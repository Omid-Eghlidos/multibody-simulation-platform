# -----------------------------
# Stage 1: Build Rust query engine
# -----------------------------
FROM rust:1.84 AS builder

# Create and set working directory inside container and copy Rust quey source code
RUN mkdir /queries
WORKDIR /queries
COPY queries .

# Clean previous builds and build Rust project in release mode
RUN cargo clean
RUN cargo build --release

# -----------------------------
# Stage 2: Build Python backend
# -----------------------------
FROM python:3.12-slim AS backend

# Install system dependencies
RUN apt-get update && apt-get install -y --no-install-recommends \
    build-essential \
 && rm -rf /var/lib/apt/lists/*

# Create working directory for backend
RUN mkdir workspace/
WORKDIR /workspace

# Copy Python requirements and install them first 
COPY app/requirements.txt ./requirements.txt
RUN pip install --no-cache-dir -r requirements.txt

COPY app ./app

# Copy compiled Rust binary from builder stage
RUN mkdir -p ./queries/target/release
COPY --from=builder /queries/target/release/sedaro-nano-queries ./queries/target/release/sedaro-nano-queries

# Expose FastAPI default port
EXPOSE 8000

# Run backend with Uvicorn (production-ready ASGI server for FastAPI)
CMD ["uvicorn", "app.app:app", "--host", "0.0.0.0", "--port", "8000", "--workers", "1"]
