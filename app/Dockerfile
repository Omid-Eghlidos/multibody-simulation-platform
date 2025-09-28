# -----------------------------
# Stage 1: Build Rust query engine
# -----------------------------
FROM rust:1.84 AS builder

# Set working directory inside container
WORKDIR /queries

# Copy the Rust query engine source code
COPY queries .

# Clean previous builds (optional but keeps image consistent)
RUN cargo clean

# Build Rust project in release mode (optimized)
RUN cargo build --release

# -----------------------------
# Stage 2: Build Python backend
# -----------------------------
FROM python:3.12-slim AS backend

# Install system dependencies (if needed for Python packages)
# Example: libpq-dev for PostgreSQL, build-essential for compiling deps
RUN apt-get update && apt-get install -y --no-install-recommends \
    build-essential \
 && rm -rf /var/lib/apt/lists/*

# Create working directory for backend
WORKDIR /app

# Copy Python requirements and install them first (for layer caching)
COPY app/requirements.txt .
RUN pip install --no-cache-dir -r requirements.txt

# Copy backend source code
COPY app .

# Create directory for Rust binary
RUN mkdir -p /queries/target/release

# Copy compiled Rust binary from builder stage
COPY --from=builder /queries/target/release/sedaro-nano-queries /queries/target/release/sedaro-nano-queries

# Expose FastAPI default port
EXPOSE 8000

# Run backend with Uvicorn (production-ready ASGI server for FastAPI)
CMD ["uvicorn", "app.app:app", "--host", "0.0.0.0", "--port", "8000", "--reload"]
