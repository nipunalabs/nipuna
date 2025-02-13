import { defineConfig } from 'vite'
import { svelte } from '@sveltejs/vite-plugin-svelte'
import tailwindcss from "@tailwindcss/vite";

// https://vite.dev/config/
export default defineConfig({
  plugins: [svelte(),
    tailwindcss(),
    {
      name: "transform-url-src",
      transformIndexHtml: (html) =>
        html
          .replace(`src="/assets/`, `src="/static/assets/`)
          .replace(`href="/`, `href="/ui/`),
    },
  ],
  build: {
    assetsDir: "static/assets",
  },
  server: {
    host: "localhost",
    proxy: {
      "/kriopy": {
        target: "http://127.0.0.1:8000",
        changeOrigin: true,
        rewrite: (path) => path.replace(/^\/nipuna/, ""),
      },
    },
  },
})
