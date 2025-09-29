#!/usr/bin/env bash
# -----------------------------------------------------------------------------
# run_compose.sh
# Cleans up old Docker containers/images/networks for this project
# and runs docker-compose with a fresh build.
# -----------------------------------------------------------------------------
# Clear the terminal for better readability
clear
# Exit on error
set -e  

# Remove old containers 
echo "- Stopping and removing old containers..."
docker-compose down -v --remove-orphans || true

# Remove any leftover containers with hardcoded names
echo "- Removing leftover containers..."
docker rm -f app web 2>/dev/null || true

echo "- Removing dangling images..."
docker image prune -f

echo "- Removing dangling volumes..."
docker volume prune -f

echo "- Building and starting services..."
docker-compose up --build
