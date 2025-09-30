# Frontend (web/)

React + TypeScript frontend for the **Multibody Simulation Platform**.  
Provides a clean interface to define initial conditions, run simulations, and visualize results.

## Features

- **Simulation form** to configure two-body initial conditions.
- **3D plots** (Plotly) for position and velocity trajectories.
- **Data table** showing initial states.
- **Radix UI** components with dark theme.
- **Modular architecture** with separated components, interfaces, and styles.
- **Vite** build system with `@` path aliases.

## Development

```bash
cd web
npm install
npm start
```
- Frontend runs at http://localhost:3030 using the Vite dev server.

## Docker

In the original Sedaro repo, the frontend was containerized by running  
`npm start` inside a Node image. That approach runs the Vite dev server  
inside the container and serves the app on port 3030.

For this project, the Dockerfile has been upgraded to a **multi-stage build**:

- Stage 1: build the React/TypeScript app with Node (`npm run build`)
- Stage 2: serve optimized static files with **Nginx** (lightweight, production-ready)

This mirrors a real production deployment while remaining simple to run.

### Usage

```bash
# Build and run frontend
docker build -t simulation-frontend ./web
docker run -p 3030:80 simulation-frontend
```
