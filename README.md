# Multibody Simulation Platform Nano (Version 1.0.0)

A professionalized refactor of **Sedaro Nano**, turning a minimal mockup into a modular, production-quality full-stack simulation system.

- **Backend:** Python FastAPI service with modular architecture (controllers, services, processors, models).  
- **Query Engine:** Rust + LALRPOP parser powering the Sedaro Nano query language.  
- **Frontend:** React + TypeScript interface for running and visualizing simulations.  

This project demonstrates how to take a research prototype and evolve it into a scalable simulation platform with testing, observability, and containerized deployment.

## 📌 Project Changes

- **Backend** (`app/`):
  - Migrated from a single-file Flask app → modular FastAPI backend with async support.  
  - Added SQLAlchemy ORM + SQLite persistence for simulation results (instead of JSON).  
  - Integrated the Rust query parser into the simulation processor.  
  - Added Prometheus observability endpoint (`/api/v1/metrics`).  
  - Dockerized backend with clean multi-stage build.  

- **Query Engine** (`queries/`):
  - Preserved and integrated the original Rust parser (LALRPOP).  
  - Connected to backend for query parsing and validation.  

- **Frontend** (`web_1/`):
  - Refactored into modular React + TypeScript (Vite).  
  - Organized into `features/`, `components/`, `pages/`, `api/`, `routes/`, `styles/`, and `interfaces`.  
  - Added proof-of-concept tests with Vitest + Testing Library (Plotly mocked).  
  - Dockerized with multi-stage build → Nginx serving.  

## 📂 Directory Structure

```sh
.
├── app/         # Python FastAPI backend
├── queries/     # Rust query parser (LALRPOP)
├── web/         # New modular frontend (React/TS, Vite)
├── docs/        # Documentation (tutorials, screenshots)
├── data/        # Runtime data (SQLite database)
├── run_backend.sh    # Run backend locally
├── test_backend.sh   # Simple curl-based backend tests
├── run_frontend.sh   # Run frontend locally
├── run_compose.sh    # Run full stack via Docker Compose
└── README.md         # Root documentation (this file)
```

## 🔗 Documentation by Component

- [Backend (app/)](app/README.md) – FastAPI backend, DB, simulation orchestration
- [Query Engine (queries/)](queries/README.md) – Rust + LALRPOP query parser
- [Frontend (web/)](web/README.md) – React/TypeScript modular frontend
- [Documentation (docs/)](docs/README.md) – Tutorials, query language guide, assets
- [Data (data/)](data/README.md) – SQLite DB and runtime artifacts

## 🚀 Quick Start

### Run Backend and Frontend Separately

```bash
# Clone repo
git clone <your-repo-url>
cd multibody-simulation-platform

# Start backend (FastAPI + SQLite)
./run_backend.sh

# Run backend tests
./test_backend.sh

# Start frontend (React/TS with Vite)
./run_frontend.sh
```
- Backend available at http://localhost:8000//api/v1/simulation/
- Frontend available at http://localhost:3030

### Run via Docker Compose

```bash
./run_compose.sh
```

## 📸 Example Output

See docs/assets/ for simulation result screenshots.
