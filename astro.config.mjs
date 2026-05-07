// @ts-check
import { defineConfig } from 'astro/config';
import sitemap from '@astrojs/sitemap';
import mdx from '@astrojs/mdx';
import vercel from '@astrojs/vercel';

export default defineConfig({
  site: 'https://finanzasclara.uk',
  output: 'static',
  trailingSlash: 'never',
  integrations: [
    sitemap({
      filter: (page) =>
        !page.includes('/legal-notice') &&
        !page.includes('/privacy-policy') &&
        !page.includes('/cookie-policy'),
      i18n: { defaultLocale: 'en', locales: { en: 'en-US' } },
    }),
    mdx(),
  ],
  adapter: vercel({
    webAnalytics: { enabled: true },
  }),
  i18n: {
    defaultLocale: 'en',
    locales: ['en'],
  },
});
