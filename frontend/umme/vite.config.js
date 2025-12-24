import { fileURLToPath, URL } from 'node:url'

import { defineConfig } from 'vite'
import vue from '@vitejs/plugin-vue'
import vueDevTools from 'vite-plugin-vue-devtools'

// https://vite.dev/config/
export default defineConfig({
  server: {
    proxy: {
      '/accounts': {
        target: 'http://127.0.0.1:8000',
        changeOrigin: true,
      },
      '/musics': {
        target: 'http://127.0.0.1:8000',
        changeOrigin: true,
      },
      '/threads': {
        target: 'http://127.0.0.1:8000',
        changeOrigin: true,
      },
      '/rag': {
        target: 'http://localhost:8000',
        changeOrigin: true,
        rewrite: path => path.replace(/^\/rag/, '/rag')
      }

    }
  },
  plugins: [
    vue(),
    vueDevTools(),
  ],
  resolve: {
    alias: {
      '@': fileURLToPath(new URL('./src', import.meta.url))
    },
  },
})
