import { defineConfig } from "vite";
import vue from "@vitejs/plugin-vue";
import prerender from "vite-plugin-prerender";
import path from "path";

export default defineConfig({
  plugins: [
    vue(),
    prerender({
      staticDir: path.resolve(__dirname, "dist"),
      routes: [
        "/", 
        "/info", 
        "/about", 
        "/athletsprofile", 
        "/traininggoal", 
        "/result",
        "/review"  // ✅ added review page
      ],
    }),
  ],
  base: "./",
  build: {
    rollupOptions: {
      output: {
        manualChunks: {
          "vue-vendor": ["vue"],
          "vuetify-lib": ["vuetify"],
          "vuetify-components": ["vuetify/components"],
          "vuetify-directives": ["vuetify/directives"],
        },
      },
    },
  },
});