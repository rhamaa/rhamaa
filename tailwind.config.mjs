import typography from '@tailwindcss/typography'

/** @type {import('tailwindcss').Config} */
export default {
  content: ['./src/**/*.{astro,html,js,jsx,md,mdx,svelte,ts,tsx,vue}'],
  theme: {
    extend: {
      colors: {
        // Atom color palette
        atom: {
          bg: '#282c34',
          'bg-light': '#2c313c',
          fg: '#abb2bf',
          'fg-dark': '#5c6370',
          green: '#98c379',
          blue: '#61afef',
          purple: '#c678dd',
          red: '#e06c75',
          orange: '#d19a66',
          cyan: '#56b6c2',
          yellow: '#e5c07b',
        },
      },
      fontFamily: {
        sans: ['IBM Plex Sans', 'sans-serif'],
        mono: ['IBM Plex Mono', 'monospace'],
      },
      boxShadow: {
        'brutal': '4px 4px 0px 0px rgba(0, 0, 0, 1)',
        'brutal-sm': '2px 2px 0px 0px rgba(0, 0, 0, 1)',
        'brutal-lg': '8px 8px 0px 0px rgba(0, 0, 0, 1)',
        'brutal-green': '4px 4px 0px 0px #98c379',
        'brutal-blue': '4px 4px 0px 0px #61afef',
        'brutal-purple': '4px 4px 0px 0px #c678dd',
        'brutal-orange': '4px 4px 0px 0px #d19a66',
      },
      borderWidth: {
        '3': '3px',
        '4': '4px',
      },
    },
  },
  plugins: [typography],
}
