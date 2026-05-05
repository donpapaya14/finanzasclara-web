"""
Plans topics avoiding duplicates and rotating categories.
Reads existing articles in src/content/blog/ to avoid repetition.
"""

import random
import re
from pathlib import Path

BLOG_DIR = Path(__file__).parent.parent / "src" / "content" / "blog"

CATEGORIES = ["savings", "investing", "debt", "budgeting", "passive-income"]

ARTICLE_FORMULAS = {
    "savings": [
        "Specific savings method with real figures in dollars/pounds and numbered steps",
        "Free app REAL name for managing money: features, how to set it up step by step",
        "Common savings mistake that costs X dollars a year with detailed calculation and fix",
        "30-day savings challenge with daily plan and expected result with real numbers",
        "Comparison of high-yield savings accounts with real bank names and current APY",
        "One automated savings trick that works on any salary with average monthly savings",
    ],
    "investing": [
        "Beginner's guide to one specific investment product with real risk and historical returns",
        "Investing mistake that loses money with real example and loss figures",
        "Explanation of one investment type (ETFs, index funds) with real performance data",
        "Comparison of free brokers for beginners with real names, fees and pros/cons",
        "How compound interest works: specific numbers over 10/20/30 years with real example",
        "Dollar-cost averaging explained with real historical data and step-by-step setup",
    ],
    "debt": [
        "Avalanche vs snowball method for paying debt with real numerical example",
        "Legal right to cancel or reduce debt with specific laws and exact deadlines",
        "True cost of a loan: how much you really pay with real APR example and calculator",
        "Negotiating debt with banks: step-by-step guide with exact phrases to use",
        "Credit card debt payoff plan: specific strategy with real timeline and savings",
    ],
    "budgeting": [
        "50/30/20 rule applied to a real salary with complete monthly example in dollars",
        "Free budgeting app with real name, how to configure it and usage example",
        "Hidden subscriptions costing you money: average annual cost and how to cancel",
        "Monthly budget template for X income with categories and percentages",
        "Zero-based budgeting explained with real example and step-by-step setup",
    ],
    "passive-income": [
        "REAL passive income source with initial investment, time required and expected monthly return",
        "Real success case of passive income: person, method, real figures and time invested",
        "Automated investment platforms with real names, returns and risks",
        "Side hustle that generates passive income with zero upfront cost and realistic earnings",
        "Dividend investing for beginners: specific stocks, yield rates and compounding example",
    ],
}


def get_existing_titles() -> set[str]:
    titles = set()
    if not BLOG_DIR.exists():
        return titles
    for md_file in BLOG_DIR.glob("*.md"):
        content = md_file.read_text(encoding="utf-8")
        match = re.search(r'^title:\s*["\']?(.+?)["\']?\s*$', content, re.MULTILINE)
        if match:
            titles.add(match.group(1).lower().strip())
    return titles


def get_category_counts() -> dict[str, int]:
    counts = {cat: 0 for cat in CATEGORIES}
    if not BLOG_DIR.exists():
        return counts
    for md_file in BLOG_DIR.glob("*.md"):
        content = md_file.read_text(encoding="utf-8")
        match = re.search(r'^category:\s*["\']?([^"\'\n]+)["\']?\s*$', content, re.MULTILINE)
        if match and match.group(1).strip() in counts:
            counts[match.group(1).strip()] += 1
    return counts


def pick_category() -> str:
    counts = get_category_counts()
    min_count = min(counts.values())
    least_covered = [cat for cat, count in counts.items() if count == min_count]
    return random.choice(least_covered)


def pick_formula(category: str) -> str:
    formulas = ARTICLE_FORMULAS.get(category, list(ARTICLE_FORMULAS.values())[0])
    return random.choice(formulas)


def plan_topic() -> dict:
    category = pick_category()
    formula = pick_formula(category)
    existing = get_existing_titles()
    return {
        "category": category,
        "formula": formula,
        "existing_titles": list(existing)[:20],
        "existing_count": len(existing),
    }
