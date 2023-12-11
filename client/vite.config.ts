import { defineConfig } from "vite";
import react from "@vitejs/plugin-react";
import { resolve } from "path";

// https://vitejs.dev/config/
export default defineConfig({
  plugins: [react()],
  resolve: {
    alias: [
      { find: "@", replacement: resolve(__dirname, "src") },
      { find: "@components", replacement: resolve(__dirname, "src/components") },
      { find: "@pages", replacement: resolve(__dirname, "src/pages") },
      { find: "@commons", replacement: resolve(__dirname, "src/commons") },
    ],
  },
});
