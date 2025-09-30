# Multiobody Simulation Platform Nano (Version 1.0.0)

The tiniest possible mockup of the simulation system. A professionalized refactor of Sedaro Nano:
- **Backend**: Python FastAPI service with modular architecture (controllers, services, processors, models).
- **Query Engine**: Rust + LALRPOP parser powering the Sedaro Nano query language.
- **Frontend**: React/TypeScript interface for running and visualizing simulations.

This project demonstrates how to take a research prototype and turn it into a production-quality full-stack simulation platform.

## 📌 Project Changes

- **Backend** (`app/`):
   - Refactored the architecture to follow professional conventions with clear separation of concerns.
   - Migrated from Flask (limited concurrency) to FastAPI for async support and scalable deployment.
   - Prepared for parallel computing to improve efficiency of simulation execution.
- **Query Engine** (`queries/`):
   - Preserved the original Rust engine for query parsing to ensure compatibility with the DSL.
- **Frontend** (`web/`):
   - Maintained original React/TypeScript structure.
   - Further improvements (interactivity, real-time playback) planned.

## 📂 Directory Structure

```sh
.
├── app/         # Python backend (FastAPI)
├── queries/     # Rust query parser (LALRPOP)
├── web/         # React/TypeScript frontend
├── docs/        # Documentation (tutorials, screenshots)
├── data/        # Runtime data (SQLite database)
├── run.sh       # Run backend service
├── test.sh      # Simple curl-based backend tests
└── README.md    # Root documentation (this file)
```

## 🔗 Documentation by Component

- [Backend (app/)](app/README.md) – FastAPI backend, DB, simulation orchestration
- [Query Engine (queries/)](queries/README.md) – Rust + LALRPOP query parser
- [Frontend (web/)](web/README.md) – React/TypeScript simulation UI
- [Documentation (docs/)](docs/README.md) – Tutorials, query language guide, assets
- [Data (data/)](data/README.md) – SQLite DB and runtime artifacts

## 🚀 Quick Start

### Run Backend and Frontend Separately

```bash
# Clone repo
git clone <your-repo-url>
cd simulations

# Start and test backend (FastAPI + SQLite)
./run_backend.sh
./test_backend.sh

# Start frontend (React/TS)
cd web
npm install
npm start
```
- Backend available at http://localhost:8000//api/v1/simulation/
- Frontend available at http://localhost:3030

### Run via Docker

```bash
docker-compose up --build
```

## 📸 Example Output

See docs/assets/ for simulation result screenshots.
