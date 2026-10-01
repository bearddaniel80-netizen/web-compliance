# web-compliance

## Description
A secured api/frontend for the AQL platform. This runs a `subprocess` on the fastapi service. There are 2 endpoints per 3 routes so in total 6 endpoints. These endpoint can also be reached with `curl -ikL localhost`.

---

## Endpoints

### /api/manifest/list
Displays all possible test files.

### /api/manifest/{filename}
Runs all tests in the test file.

### /api/suite/list
Displays all possible suite files.

### /api/suite/{filename}
Runs all tests in the test files.

### /api/tag/list
Displays all possible test tags.

### /api/tag/{tag}
Runs all tests across test files with test tag.

---

## To run

### Start services
```bash
docker compose up --build
```

### View frontend
[localhost](https://localhost)

### Health check
```bash
curl -ikL localhost/health
```

### Call API
```bash
curl -ikL localhost/api/data
```

### Run playwrite tests
```bash
docker compose --profile test up
```

### Stop services
```bash
docker compose down
```

### Cleanup docker
```bash
docker volume prune && docker system prune
```
---

## Services

### Caddy
Reverse proxy with additional rate limit plugin. Manages self-signed ssl certificates.

### FastAPI
A python based api only gateway protected by docker secrets file. Being python based, can use `subprocess` function to make external calls to AQL platform applications.

### Frontend
A React simple page that displays api data.

### Node
A nodejs express BFF (backend for frontend) gateway protected by docker secrets file.

### Playwrite
Tests browser and api.

---

## Creating docker secrets
```bash
openssl rand -hex 32
```

---

## How docker secrets are shared
```text
             Docker secret
                  │
          ┌───────┴────────┐
          ▼                ▼
       Node.js           FastAPI
          │                │
          └── same key ────┘
```

---
## Network Flow

```text
                  PUBLIC
        ┌───────────┼───────────┐
        │           │           │
      Caddy      frontend     MinIO
        │                       │
        │                       │
        └───────────────────────┘

                  BACKEND
        ┌───────────┼───────────┐
        │           │           │
       Node      FastAPI       MinIO
```
---

## System Flow

```text
Frontend
  ↓
Caddy
  ↓
Node
  ↓
FastAPI
```

## Reference
This is a web implementation of a [CLI tool](https://github.com/bearddaniel80-netizen/compliance-public.git).