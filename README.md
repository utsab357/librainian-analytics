<!-- README generated and enhanced for GitHub display -->
# Za — Django Analytics Demo ⚡

[![Python](https://img.shields.io/badge/python-3.8%2B-blue)](https://www.python.org/)
[![Django](https://img.shields.io/badge/django-5.2.7-green)](https://www.djangoproject.com/)
[![DRF](https://img.shields.io/badge/djangorestframework-3.16.1-orange)](https://www.django-rest-framework.org/)
[![License](https://img.shields.io/badge/license-MIT-lightgrey)](#license)

A compact Django project showcasing analytics patterns, REST APIs, and a demo-data loader. Designed for fast local setup and experimentation.

Table of Contents
- [Features](#features)
- [Tech Stack](#tech-stack)
- [Quick Start (Windows / PowerShell)](#quick-start-windows--powershell)
- [API & Developer Notes](#api--developer-notes)
- [Demo Data](#demo-data)
- [Testing](#testing)
- [VS Code Tips](#vs-code-tips)
- [Project Layout](#project-layout)
- [Troubleshooting](#troubleshooting)
- [Contributing](#contributing)
- [License](#license)

## Features

- Ready-to-run Django project (SQLite for local development)
- Django REST Framework endpoints and serializers
- Demo-data management command for fast testing
- Examples for querying APIs using `curl` / `httpie` / Python `requests`

## Tech Stack

- Python 3.8+
- Django 5.2.7
- Django REST Framework
- SQLite (development)
- See `requirements.txt` for full dependency list

## Quick Start (Windows / PowerShell)

1. Create and activate a virtual environment

```powershell
python -m venv .venv
.\.venv\Scripts\Activate.ps1
```

2. Install project dependencies

```powershell
pip install -r requirements.txt
```

3. Apply database migrations

```powershell
python manage.py migrate
```

4. (Optional) Create a superuser to access the admin

```powershell
python manage.py createsuperuser
```

5. Start the development server

```powershell
python manage.py runserver
```

Open `http://127.0.0.1:8000/` or the API docs (see below).

## API & Developer Notes

- The project uses Django REST Framework. If `drf-yasg` is enabled in `urls.py`, Swagger UI is commonly available at `/swagger/` or `/swagger/?format=openapi`.
- To discover routes quickly, check `analytics/urls.py` and `librainian_analytics/urls.py`.

Example requests

curl (JSON):

```bash
curl -sS -H "Accept: application/json" http://127.0.0.1:8000/api/your-endpoint/
```

httpie:

```bash
http GET http://127.0.0.1:8000/api/your-endpoint/
```

Python `requests` example:

```python
import requests

resp = requests.get('http://127.0.0.1:8000/api/your-endpoint/')
print(resp.status_code)
print(resp.json())
```

Replace `your-endpoint` with a real route from `analytics/urls.py`.

### API Endpoints (examples)

Run the server locally with:

```powershell
python manage.py runserver
```

When running locally the `{{base_url}}` value is typically `http://127.0.0.1:8000` (or your host/port). Below are common analytics endpoints present in this project and short descriptions — use these for quick API checks, Postman collections, or automated scripts.

- `{{base_url}}/api/analytics/engagement-overview/`
  - Description: High-level engagement metrics (active users, sessions, avg session duration, retention snapshots).
  - Query params (common): `start_date`, `end_date`, `period` (e.g. `7d`, `30d`).

- `{{base_url}}/api/analytics/financial-snapshot/`
  - Description: Revenue, refunds, AR, and quick financial KPIs for the selected period.
  - Query params: `period` (e.g. `3m`, `6m`, `12m`), `start_date`, `end_date`.

- `{{base_url}}/api/analytics/charts/gender-distribution/`
  - Description: Returns counts/percentages by gender — suitable for pie/bar charts.

- `{{base_url}}/api/analytics/key-stats/`
  - Description: Summary KPIs (total students, active courses, conversion rate, MRR/ARR snapshots).

- `{{base_url}}/api/analytics/charts/monthly-revenue/?period=3m`
  - Description: Time-series monthly revenue points. `period` controls range (examples: `3m`, `6m`, `12m`).

- `{{base_url}}/api/analytics/charts/enrollment-trends/?period=3m`
  - Description: Enrollment counts over time (useful for trend lines and forecasts).

- `{{base_url}}/api/analytics/revenue-visitors/`
  - Description: Combines revenue and visitor metrics to compute ratios like revenue-per-visitor.

- `{{base_url}}/api/analytics/students-by-area/`
  - Description: Geographic breakdown of students (country / region / area) suitable for maps or tables.

- `{{base_url}}/api/analytics/charts/visitor-analytics/?period=3m`
  - Description: Visitor metrics (new vs returning, sessions, bounce rate) returned as chart-friendly time series.

Notes:
- Replace `{{base_url}}` with your running server address (for local dev: `http://127.0.0.1:8000`).
- The above endpoints return JSON and usually accept `Accept: application/json` header.
- Exact field names in responses depend on the serializers defined in `analytics/serializers.py` — inspect those files to map JSON fields to UI elements or scripts.

Authentication
 - This project lists `djangorestframework_simplejwt` in `requirements.txt`. If the API requires authentication, you can obtain an access token (common default endpoints when using SimpleJWT are `/api/token/` and `/api/token/refresh/`) then include it in requests:

1. Obtain token (example):

```bash
curl -sS -X POST "{{base_url}}/api/token/" -H "Content-Type: application/json" -d '{"username":"<user>","password":"<pass>"}'
# Response contains `access` and `refresh` tokens
```

2. Use token in a request:

```bash
curl -sS -H "Accept: application/json" -H "Authorization: Bearer <ACCESS_TOKEN>" "http://127.0.0.1:8000/api/analytics/engagement-overview/"
```

Examples (quick checks)

```bash
# Replace base_url with your server address (local example shown)
BASE=http://127.0.0.1:8000

# Simple GET
curl -sS -H "Accept: application/json" "$BASE/api/analytics/key-stats/"

# With query param
curl -sS -H "Accept: application/json" "$BASE/api/analytics/charts/monthly-revenue/?period=3m"

# With JWT authorization (set ACCESS_TOKEN first)
curl -sS -H "Accept: application/json" -H "Authorization: Bearer $ACCESS_TOKEN" "$BASE/api/analytics/revenue-visitors/"
```

If you want, I can:
- add a Postman/Insomnia collection JSON to the repo with these endpoints prefilled,
- add a short example React/JS snippet that fetches `key-stats` and renders a tiny chart, or
- inspect `analytics/serializers.py` and create a compact API reference table listing each endpoint's response fields.


## Demo Data

Populate the database with demo/test data using the included management command:

```powershell
python manage.py load_demo_data
```

The command is implemented at `analytics/management/commands/load_demo_data.py` and is useful to bootstrap example records for UI/API testing.

## Testing

Run the test suite with Django's test runner:

```powershell
python manage.py test
# or run tests for the analytics app only
python manage.py test analytics
```

Consider running tests in isolation during development and using `pytest` if you prefer (not configured by default).

## VS Code Tips (look good & productive)

- Recommended extensions:
  - `ms-python.python` (Python language support)
  - `batisteo.vscode-django` or similar Django helpers
  - `eamodio.gitlens` (Git insights)
  - `yzhang.markdown-all-in-one` (Markdown preview & shortcuts)

- Open the Markdown preview to see the README rendered: `Ctrl+Shift+V` (or `Ctrl+K V`).
- Useful `settings.json` snippets to add to your workspace for consistent environment:

```json
{
  "python.pythonPath": ".venv\\Scripts\\python.exe",
  "python.formatting.provider": "black",
  "editor.formatOnSave": true
}
```

## Project Layout

- `manage.py` — Django CLI entrypoint
- `db.sqlite3` — SQLite database (development)
- `requirements.txt` — pinned Python dependencies
- `analytics/` — main app (models, views, serializers, urls)
  - `management/commands/load_demo_data.py` — demo data loader
- `librainian_analytics/` — Django project (settings, urls, wsgi)

## Troubleshooting

- If migrations fail locally, you can remove `db.sqlite3` (development only) and re-run migrations:

```powershell
del db.sqlite3
python manage.py migrate
```

- Dependency issues: recreate the virtualenv and reinstall packages.
- If you see import errors related to environment variables, verify `.env` usage (this project uses `python-decouple` — check `settings.py`).

## Contributing

- Please open issues for bugs or feature requests.
- For code changes: fork, create a branch, add tests, and open a pull request.
- Keep changes focused and include tests where appropriate.

## License

This repository is currently unlicensed in the tree — add a `LICENSE` file to declare a license (for example, MIT).

---

If you'd like, I can:

- add a `CONTRIBUTING.md` with contribution guidelines,
- add a `LICENSE` file (MIT/Apache/etc.), or
- add GitHub Actions to run tests on push and display a passing/failing badge.

Enjoy exploring the project — open an issue if you want help running it locally! 🚀

