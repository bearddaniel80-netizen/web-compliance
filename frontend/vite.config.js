
import { defineConfig } from "vite";
import react from "@vitejs/plugin-react";
import { resolve } from "path";
import { fileURLToPath } from "url";

const root = fileURLToPath(new URL(".", import.meta.url));

export default defineConfig({
  plugins: [react()],

  base: "/",

  build: {
    outDir: "dist",
    emptyOutDir: true,

    rollupOptions: {
      input: {
        index: resolve(root, "index.html"),
        cache: resolve(root, "feature/cache.html"),
        failfast: resolve(root, "feature/failfast.html"),
        query: resolve(root, "feature/failfast-query.html"),
        profile: resolve(root, "feature/profile.html"),
        retry: resolve(root, "feature/retry.html"),
        github: resolve(root, "format/github.html"),
        html: resolve(root, "format/html.html"),
        json: resolve(root, "format/json.html"),
        markdown: resolve(root, "format/markdown.html"),
        pdf: resolve(root, "format/pdf.html"),
      }
    }
  }
});
