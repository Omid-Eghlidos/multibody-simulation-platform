#!/bin/bash
# test.sh
# End-to-end smoke test for Sedaro Nano backend

BASE_URL="http://localhost:8000/api/v1/simulation"

# Health check
echo "1) Health check..."
curl -s -o /dev/null -w "Status: %{http_code}\n" "$BASE_URL/"

# Run simulation with default parameters
echo -e "\n2) Run simulation..."
curl -s -X POST "$BASE_URL/run" \
    -H "Content-Type: application/json" \
    -d '{
        "Body1": {
            "time": 0.0,
            "timeStep": 0.01,
            "position": {"x": -0.73, "y": 0.0, "z": 0.0},
            "velocity": {"x": 0.0, "y": -0.0015, "z": 0.0},
            "mass": 1.0
        },
        "Body2": {
            "time": 0.0,
            "timeStep": 0.01,
            "position": {"x": 60.34, "y": 0.0, "z": 0.0},
            "velocity": {"x": 0.0, "y": 0.13, "z": 0.0},
            "mass": 0.123
        }
    }' | jq .

# Get latest simulation
echo -e "\n3) Get latest simulation..."
curl -s "$BASE_URL/latest" | jq .
