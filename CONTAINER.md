# Containerized version

Build and run the repository container with Docker Compose:

```bash
docker compose build
docker compose up
```

Persistent data and logs use named volumes. The native implementations remain unchanged.

Interactive diagnostics:

```bash
docker compose run --rm bizxtreme-app bash
```

The image runs as a non-root user. Desktop/GUI components should use their service, headless, or CLI modes in containers.
