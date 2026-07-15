FROM python:3.13-slim@sha256:bffeb7bd6a85767587059c6ba23e1e9122078e3aa3fa836099171b9bb5a9bb00

# Install test runtime only (no network at container runtime)
RUN pip install --no-cache-dir pytest==8.4.1

WORKDIR /app

# Only copy the input log into the build context; do not include any precomputed report.json
COPY data/access.log /app/access.log
