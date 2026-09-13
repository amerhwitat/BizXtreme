FROM ubuntu:24.04
ENV DEBIAN_FRONTEND=noninteractive PYTHONUNBUFFERED=1
RUN apt-get update && apt-get install -y --no-install-recommends bash ca-certificates curl git python3 python3-pip python3-venv nodejs npm openjdk-21-jdk-headless gcc g++ make cmake pkg-config rustc cargo && rm -rf /var/lib/apt/lists/*
WORKDIR /app
COPY . /app
COPY docker/entrypoint.sh /usr/local/bin/repo-entrypoint
RUN chmod +x /usr/local/bin/repo-entrypoint && useradd -m -u 10001 appuser && chown -R appuser:appuser /app
USER appuser
EXPOSE 8000 8080
ENTRYPOINT ["/usr/local/bin/repo-entrypoint"]
