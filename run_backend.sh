#!/bin/bash
# run_backend.sh
# Launches the FastAPI backend using Uvicorn with live reload

uvicorn app.app:app --host 0.0.0.0 --port 8000 --reload

