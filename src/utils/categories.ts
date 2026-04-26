export const CATEGORIES = {
  'ahorro': { name: 'Ahorro', slug: 'ahorro', description: 'Estrategias de ahorro con resultados reales' },
  'inversion': { name: 'Inversion', slug: 'inversion', description: 'Invertir desde cero con datos concretos' },
  'deudas': { name: 'Deudas', slug: 'deudas', description: 'Salir de deudas con metodos probados' },
  'presupuesto': { name: 'Presupuesto', slug: 'presupuesto', description: 'Gestionar tu dinero mes a mes' },
  'ingresos-pasivos': { name: 'Ingresos Pasivos', slug: 'ingresos-pasivos', description: 'Generar ingresos extra con evidencia' },
} as const;

export type Category = keyof typeof CATEGORIES;

export function getCategoryName(cat: Category): string {
  return CATEGORIES[cat].name;
}

export function getCategoryBadgeClass(cat: Category): string {
  return `badge badge--${cat}`;
}
