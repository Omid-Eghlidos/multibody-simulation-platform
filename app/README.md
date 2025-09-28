# Backend (app/)

The Python FastAPI backend for Sedaro Nano (Refactored).  
Implements simulation services, database persistence, and API endpoints.

## Structure

- **controllers/** – API routers  
- **services/** – business logic  
- **processors/** – simulation orchestration  
- **models/** – ORM models (SQLAlchemy)  
- **clients/** – database client  
- **config/** – settings and configs  
- **utilities/** – constants, messages, math, data structures  

## Setup

```bash
# Run backend separately
./run.sh
```
- API: http://localhost:8000
- Endpoints: /api/v1/simulation (/run, /latest, /health)

## Notes

- SQLite DB is auto-created in data/database.db.
- Future: extend simulation_processor.py with full physics logic.
