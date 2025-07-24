FROM python:3.12-slim

# Install dependencies
RUN apt-get update && apt-get install -y curl tar

# Download and install the ARM64 uv binary
RUN curl -sSL https://github.com/astral-sh/uv/releases/latest/download/uv-aarch64-unknown-linux-gnu.tar.gz \
    | tar -xz && \
    mv uv-aarch64-unknown-linux-gnu/uv /usr/local/bin/uv && \
    chmod +x /usr/local/bin/uv && \
    rm -rf uv-aarch64-unknown-linux-gnu

# Set working directory
WORKDIR /app

# Copy and install dependencies
COPY pyproject.toml .
RUN uv pip install . --system

# Copy the rest of the app
COPY . .

# Run the app
CMD ["uv", "run", "python", "-m", "digesting_feed.main"]
