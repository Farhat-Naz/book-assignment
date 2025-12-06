import {themes as prismThemes} from 'prism-react-renderer';
import type {Config} from '@docusaurus/types';
import type * as Preset from '@docusaurus/preset-classic';

const math = require('remark-math');
const katex = require('rehype-katex');

const config: Config = {
  title: 'Physical AI & Humanoid Robotics',
  tagline: 'A Comprehensive Course on Humanoid Robotics, AI, and Embodied Intelligence',
  favicon: 'img/favicon.ico',

  // Future flags for Docusaurus v4 compatibility
  future: {
    v4: true,
  },

  // Production URL - Update with your actual deployment URL
  url: 'https://humanoid-robotics-course.vercel.app',
  baseUrl: '/',

  // GitHub pages deployment config
  organizationName: 'your-org', // Update with your GitHub org/user
  projectName: 'humanoid-robotics', // Update with your repo name

  onBrokenLinks: 'throw',
  onBrokenMarkdownLinks: 'warn',

  // Internationalization config
  i18n: {
    defaultLocale: 'en',
    locales: ['en'],
  },

  // Markdown configuration for Mermaid diagrams
  markdown: {
    mermaid: true,
  },

  // Themes including Mermaid support
  themes: ['@docusaurus/theme-mermaid'],

  presets: [
    [
      'classic',
      {
        docs: {
          sidebarPath: './sidebars.ts',
          routeBasePath: '/', // Serve docs at the site's root
          // Add remark and rehype plugins for math equations
          remarkPlugins: [math],
          rehypePlugins: [katex],
          // Show last update time
          showLastUpdateTime: true,
          // Edit URL - Update with your repo
          editUrl: 'https://github.com/your-org/humanoid-robotics/edit/main/',
        },
        blog: false, // Disable blog for this course site
        theme: {
          customCss: './src/css/custom.css',
        },
      } satisfies Preset.Options,
    ],
  ],

  // KaTeX stylesheet for math rendering
  stylesheets: [
    {
      href: 'https://cdn.jsdelivr.net/npm/katex@0.16.9/dist/katex.min.css',
      type: 'text/css',
      integrity: 'sha384-n8MVd4RsNIU0tAv4ct0nTaAbDJwPJzDEaqSD1odI+WdtXRGWt2kTvGFasHpSy3SV',
      crossorigin: 'anonymous',
    },
  ],

  themeConfig: {
    image: 'img/social-card.jpg',

    // Color mode configuration
    colorMode: {
      defaultMode: 'light',
      disableSwitch: false,
      respectPrefersColorScheme: true,
    },

    // Navbar configuration
    navbar: {
      title: 'Physical AI & Humanoid Robotics',
      logo: {
        alt: 'Course Logo',
        src: 'img/logo.svg',
      },
      items: [
        {
          type: 'docSidebar',
          sidebarId: 'courseSidebar',
          position: 'left',
          label: 'Course',
        },
        {
          to: '/prerequisites',
          label: 'Prerequisites',
          position: 'left',
        },
        {
          to: '/glossary',
          label: 'Glossary',
          position: 'right',
        },
        {
          href: 'https://github.com/your-org/humanoid-robotics',
          label: 'GitHub',
          position: 'right',
        },
      ],
    },

    // Footer configuration
    footer: {
      style: 'dark',
      links: [
        {
          title: 'Course',
          items: [
            {
              label: 'Module 1: Foundations',
              to: '/module-01-foundations',
            },
            {
              label: 'Module 2: Kinematics',
              to: '/module-02-kinematics',
            },
            {
              label: 'Prerequisites',
              to: '/prerequisites',
            },
          ],
        },
        {
          title: 'Resources',
          items: [
            {
              label: 'Datasets',
              to: '/resources/datasets',
            },
            {
              label: 'Tools Setup',
              to: '/resources/tools-setup',
            },
            {
              label: 'Glossary',
              to: '/glossary',
            },
          ],
        },
        {
          title: 'Community',
          items: [
            {
              label: 'GitHub Discussions',
              href: 'https://github.com/your-org/humanoid-robotics/discussions',
            },
            {
              label: 'Report Issue',
              href: 'https://github.com/your-org/humanoid-robotics/issues',
            },
          ],
        },
      ],
      copyright: `Copyright © ${new Date().getFullYear()} Physical AI & Humanoid Robotics Course. Licensed under CC BY-NC-SA 4.0.`,
    },

    // Prism syntax highlighting
    prism: {
      theme: prismThemes.github,
      darkTheme: prismThemes.dracula,
      additionalLanguages: ['bash', 'python', 'cpp', 'yaml', 'json'],
    },

    // Mermaid theme configuration
    mermaid: {
      theme: {light: 'neutral', dark: 'dark'},
    },

    // Algolia search configuration (to be configured later)
    // algolia: {
    //   appId: 'YOUR_APP_ID',
    //   apiKey: 'YOUR_SEARCH_API_KEY',
    //   indexName: 'humanoid-robotics',
    // },

  } satisfies Preset.ThemeConfig,
};

export default config;
