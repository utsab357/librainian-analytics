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

