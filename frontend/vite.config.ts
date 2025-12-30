import { defineConfig } from "vite";
import tailwindcss from "@tailwindcss/vite";
import { resolve } from "path";

export default defineConfig(({ mode }) => {
  const isProd = mode === "production";

  return {
    plugins: [tailwindcss()],
    base: "/static/build/",

    server: {
      host: true,
      port: 5173,
      strictPort: true,
      hmr: { host: "localhost", port: 5173 },
    },

    // Cache mais eficiente
    optimizeDeps: {
      // pré-bundle de deps melhora o start do dev server
      // (se quiser, posso sugerir includes depois que você listar deps)
    },

    build: {
      outDir: resolve(__dirname, "../static/build"),
      emptyOutDir: true,
      manifest: true,

      // Performance de build
      target: "es2019",
      sourcemap: !isProd,        // não gerar sourcemap em prod
      minify: "esbuild",         // rápido
      cssMinify: "esbuild",      // rápido
      reportCompressedSize: false, // acelera build

      // chunking (melhora cache do browser)
      rollupOptions: {
        input: resolve(__dirname, "index.html"),
        output: {
          manualChunks(id) {
            if (id.includes("node_modules")) {
              // opcional: separar vendor pra cache longo
              return "vendor";
            }
          },
        },
      },
    },
  };
});
