export const CATEGORIES = {
  'savings': { name: 'Savings', slug: 'savings', description: 'Save more money every month' },
  'investing': { name: 'Investing', slug: 'investing', description: 'Grow your wealth with real data' },
  'debt': { name: 'Debt', slug: 'debt', description: 'Pay off debt faster' },
  'budgeting': { name: 'Budgeting', slug: 'budgeting', description: 'Control your spending' },
  'passive-income': { name: 'Passive Income', slug: 'passive-income', description: 'Build income streams' }
} as const;

export type Category = keyof typeof CATEGORIES;

export function getCategoryName(cat: Category): string {
  return CATEGORIES[cat].name;
}

export function getCategoryBadgeClass(cat: Category): string {
  return `badge badge--${cat}`;
}
