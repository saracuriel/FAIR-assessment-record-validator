# ---------- Stage 1: Build Rudof ----------
FROM rustlang/rust:nightly AS rudof-builder

WORKDIR /build

RUN git clone https://github.com/rudof-project/rudof.git
WORKDIR /build/rudof

# Ensure nightly is active
RUN rustup default nightly

# Build only the CLI binary (important!)
RUN cargo build --release --bin rudof

# ---------- Stage 2: Python + FastAPI ----------
FROM python:3.11-slim

RUN apt-get update && apt-get install -y \
    ca-certificates \
    && rm -rf /var/lib/apt/lists/*

# Copy Rudof binary only
COPY --from=rudof-builder /build/rudof/target/release/rudof /usr/local/bin/rudof
RUN chmod +x /usr/local/bin/rudof

WORKDIR /app
COPY requirements.txt .
RUN pip install --no-cache-dir -r requirements.txt

COPY app/ ./app/

EXPOSE 8000

CMD ["uvicorn", "app.main:app", "--host", "0.0.0.0", "--port", "8000"]
