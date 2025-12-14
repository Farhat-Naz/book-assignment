import {themes as prismThemes} from 'prism-react-renderer';
import type {Config} from '@docusaurus/types';
import type * as Preset from '@docusaurus/preset-classic';

// This runs in Node.js - Don't use client-side code here (browser APIs, JSX...)

const config: Config = {
  title: 'Physical AI & Humanoid Robotics',
  tagline: 'Master Physical AI, Humanoid Robotics, ROS 2, and Autonomous Systems',
  favicon: 'img/favicon.ico',

  // Future flags, see https://docusaurus.io/docs/api/docusaurus-config#future
  future: {
    v4: true, // Improve compatibility with the upcoming Docusaurus v4
  },

  // Set the production url of your site here
  // Support Railway, Vercel, and GitHub Pages deployments
  url: process.env.RAILWAY_PUBLIC_DOMAIN
    ? `https://${process.env.RAILWAY_PUBLIC_DOMAIN}`
    : process.env.VERCEL_URL
    ? `https://${process.env.VERCEL_URL}`
    : 'https://farhat-naz.github.io',
  // Set the /<baseUrl>/ pathname under which your site is served
  // For Railway/Vercel deployment use '/', for GitHub pages use '/<projectName>/'
  baseUrl: '/',

  // GitHub pages deployment config.
  // If you aren't using GitHub pages, you don't need these.
  organizationName: 'Farhat-Naz', // Usually your GitHub org/user name.
  projectName: 'newhumandiod-book', // Usually your repo name.
  deploymentBranch: 'gh-pages',
  trailingSlash: false,

  onBrokenLinks: 'warn',

  // Multilingual support - currently only English enabled
  // Other languages (Urdu, Arabic, Chinese) will be enabled after backend translation service is deployed
  i18n: {
    defaultLocale: 'en',
    locales: ['en'], // Only English for now
    localeConfigs: {
      en: {
        label: 'English',
        direction: 'ltr',
      },
      // Disabled until translation service is ready:
      // ur: { label: 'اردو', direction: 'rtl' },
      // ar: { label: 'العربية', direction: 'rtl' },
      // zh: { label: '中文', direction: 'ltr' },
    },
  },

  // Mermaid for diagrams
  markdown: {
    mermaid: true,
  },
  themes: ['@docusaurus/theme-mermaid'],

  presets: [
    [
      'classic',
      {
        docs: {
          sidebarPath: './sidebars.ts',
          // Please change this to your repo.
          // Remove this to remove the "edit this page" links.
          editUrl:
            'https://github.com/physicalai/book-assignment',
        },
        blog: {
          showReadingTime: true,
          feedOptions: {
            type: ['rss', 'atom'],
            xslt: true,
          },
          // Please change this to your repo.
          // Remove this to remove the "edit this page" links.
          editUrl:
            'https://github.com/physicalai/book-assignment',
          // Useful options to enforce blogging best practices
          onInlineTags: 'warn',
          onInlineAuthors: 'warn',
          onUntruncatedBlogPosts: 'warn',
        },
        theme: {
          customCss: './src/css/custom.css',
        },
      } satisfies Preset.Options,
    ],
  ],

  themes: ['@docusaurus/theme-mermaid'],

  themeConfig: {
    // Replace with your project's social card
    image: 'img/logo.svg',
    colorMode: {
      respectPrefersColorScheme: true,
    },
    navbar: {
      title: 'Physical AI & Robotics',
      logo: {
        alt: 'Physical AI Logo',
        src: 'img/logo.svg',
      },
      items: [
        {
          type: 'docSidebar',
          sidebarId: 'tutorialSidebar',
          position: 'left',
          label: 'Course',
        },
        {to: '/blog', label: 'Blog', position: 'left'},
        // Locale dropdown disabled until translation service is deployed
        // {
        //   type: 'localeDropdown',
        //   position: 'right',
        // },
        {
          href: 'https://github.com/physicalai/book-assignment',
          label: 'GitHub',
          position: 'right',
        },
      ],
    },
    footer: {
      style: 'dark',
      links: [
        {
          title: 'Course',
          items: [
            {
              label: 'Get Started',
              to: '/docs/intro',
            },
            {
              label: 'Module 1',
              to: '/docs/category/module-1',
            },
            {
              label: 'Module 2',
              to: '/docs/category/module-2',
            },
          ],
        },
        {
          title: 'Community',
          items: [
            {
              label: 'GitHub Discussions',
              href: 'https://github.com/physicalai/book-assignment/discussions',
            },
            {
              label: 'Issues',
              href: 'https://github.com/physicalai/book-assignment/issues',
            },
          ],
        },
        {
          title: 'More',
          items: [
            {
              label: 'Blog',
              to: '/blog',
            },
            {
              label: 'GitHub',
              href: 'https://github.com/physicalai/book-assignment',
            },
          ],
        },
      ],
      copyright: `Copyright © ${new Date().getFullYear()} Physical AI & Humanoid Robotics. Built with Docusaurus.`,
    },
    prism: {
      theme: prismThemes.github,
      darkTheme: prismThemes.dracula,
      additionalLanguages: ['python', 'bash', 'yaml', 'cpp', 'cmake', 'json', 'docker'],
    },
  } satisfies Preset.ThemeConfig,
};

export default config;
