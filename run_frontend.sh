#!/bin/bash
# run_frontend.sh
# Launches the React frontend using Vite with live reload

set -euo pipefail

# Go to frontend directory
cd "$(dirname "$0")/web"

# Install dependencies if node_modules is missing
if [ ! -d "node_modules" ]; then
  echo "- Installing dependencies..."
  npm install
fi

# Start Vite dev server
echo "- Starting frontend (Vite)..."
npm start
