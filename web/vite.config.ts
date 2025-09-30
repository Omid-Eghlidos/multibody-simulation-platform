import { defineConfig } from 'vite';
import react from '@vitejs/plugin-react';
import svgr from 'vite-plugin-svgr';
import tsconfigPaths from 'vite-tsconfig-paths';

// https://vitejs.dev/config/
export default defineConfig({
    base: '/',
    plugins: [
        react(),
        tsconfigPaths(), // reads "paths" from tsconfig.json (e.g., @/* → src/*)
        svgr()
    ],
    server: {
        host: true,
        port: 3030,
    },
});
