import { defineConfig } from 'vite'
import vue from '@vitejs/plugin-vue'
import Components from 'unplugin-vue-components/vite'
import { ElementPlusResolver } from 'unplugin-vue-components/resolvers'
import AutoImport from 'unplugin-auto-import/vite'
import 'd3'



// https://vitejs.dev/config/
export default defineConfig({
  plugins: [
    vue(),
    Components({
      // your plugin installation
      resolvers: [
        ElementPlusResolver(),
       ],
    }),
    AutoImport({ 
      imports: [
        'vue','vue-router','pinia'
      ]
    }),
  ],
})
