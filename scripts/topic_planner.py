"""
Planifica temas evitando duplicados y rotando categorías.
Lee artículos existentes en src/content/blog/ para evitar repetir.
"""

import os
import random
import re
from pathlib import Path

BLOG_DIR = Path(__file__).parent.parent / "src" / "content" / "blog"

CATEGORIES = ["ahorro", "inversion", "deudas", "presupuesto", "ingresos-pasivos"]

ARTICLE_FORMULAS = {
    "ahorro": [
        "Metodo de ahorro concreto con cifras reales en euros y pasos numerados",
        "App gratuita REAL para gestionar dinero: nombre, funciones, como usarla paso a paso",
        "Error de ahorro comun que cuesta X euros al ano con calculo detallado",
        "Reto de ahorro de 30 dias con plan diario y resultado esperado con cifras",
        "Comparativa de cuentas de ahorro remuneradas con nombres reales y TAE actual",
    ],
    "inversion": [
        "Guia de inversion para principiantes con un producto concreto, riesgo real y rendimiento historico",
        "Error de inversion que pierde dinero con ejemplo real y cifras de perdida",
        "Explicacion de un tipo de inversion (ETFs, fondos indexados, etc.) con datos de rendimiento real",
        "Comparativa de brokers gratuitos para principiantes con nombres, comisiones y pros/contras reales",
    ],
    "deudas": [
        "Metodo avalancha vs bola de nieve para pagar deudas con ejemplo numerico real",
        "Derecho legal de cancelacion de deuda con articulos de ley y plazos concretos",
        "Calculadora de deuda: cuanto pagas realmente por un prestamo con ejemplo de TAE real",
        "Negociacion de deuda con bancos: guia paso a paso con frases exactas a usar",
    ],
    "presupuesto": [
        "Metodo 50/30/20 aplicado con salario real y ejemplo mensual completo en euros",
        "App gratuita de presupuesto REAL con nombre, como configurarla y ejemplo de uso",
        "Gastos hormiga que te cuestan X euros al ano con lista concreta y alternativas",
        "Plan de presupuesto mensual para sueldo de X euros con categorias y porcentajes",
    ],
    "ingresos-pasivos": [
        "Fuente de ingreso pasivo REAL con inversion inicial, tiempo y rendimiento mensual esperado",
        "Caso de exito real de ingreso pasivo: persona, metodo, cifras y tiempo invertido",
        "Plataformas de inversion automatizada REALES con nombres, rendimientos y riesgos",
    ],
}


def get_existing_titles() -> set[str]:
    """Lee títulos de artículos existentes del frontmatter."""
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
    """Cuenta artículos por categoría."""
    counts = {cat: 0 for cat in CATEGORIES}
    if not BLOG_DIR.exists():
        return counts

    for md_file in BLOG_DIR.glob("*.md"):
        content = md_file.read_text(encoding="utf-8")
        match = re.search(r'^category:\s*["\']?(\w+)["\']?\s*$', content, re.MULTILINE)
        if match and match.group(1) in counts:
            counts[match.group(1)] += 1
    return counts


def pick_category() -> str:
    """Elige categoría con menos artículos (rotación equilibrada)."""
    counts = get_category_counts()
    min_count = min(counts.values())
    least_covered = [cat for cat, count in counts.items() if count == min_count]
    return random.choice(least_covered)


def pick_formula(category: str) -> str:
    """Elige fórmula aleatoria para la categoría."""
    formulas = ARTICLE_FORMULAS.get(category, ARTICLE_FORMULAS["nutricion"])
    return random.choice(formulas)


def plan_topic() -> dict:
    """Devuelve categoría y fórmula para el próximo artículo."""
    category = pick_category()
    formula = pick_formula(category)
    existing = get_existing_titles()

    return {
        "category": category,
        "formula": formula,
        "existing_titles": list(existing)[:20],  # Para contexto al AI
        "existing_count": len(existing),
    }
