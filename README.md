# Django Todo List App

A simple Todo List web application built with Django. This repository contains a minimal Django project that demonstrates creating, completing, and deleting todo items with a small, easily-modified codebase.

## Quick summary

- Framework: Django (project includes a local `env/` with Django installed)
- Database: SQLite (`db.sqlite3`)
- Purpose: Learning/demo app for Django basics — views, templates, simple CRUD

## Features

- Add new todo items
- Mark items as complete
- Delete items
- Simple home page rendering: see `templates/home.html`

## Tech stack

- Python 3.10+ (recommended)
- Django 5.x (installed in the provided `env`)
- SQLite (built-in with Django; database file `db.sqlite3`)

## Project structure (top-level)

- `manage.py` — Django management script
- `todo_project/` — Django project module (settings, urls, views, wsgi/asgi)
- `templates/` — HTML templates (e.g. `templates/home.html`)
- `db.sqlite3` — SQLite database used in development
- `env/` — (optional) virtual environment included in the repo

If you open the repository you'll find the main app logic inside `todo_project/` and the template(s) under `templates/`.

## Prerequisites

- Python 3.10 or newer
- (Optional) Git if you plan to clone or contribute
- On Windows PowerShell you may need to allow script execution for the virtual environment activation in the current session:

```powershell
# (one-time per session) allow local scripts to run
Set-ExecutionPolicy -ExecutionPolicy RemoteSigned -Scope Process
```

## Setup (Windows / PowerShell)

1. Activate the included virtual environment (if you want to use the provided `env`):

```powershell
.\env\Scripts\Activate.ps1
```

Or create & use a fresh virtualenv:

```powershell
python -m venv env
.\env\Scripts\Activate.ps1
```

2. Install dependencies

If this repo has a `requirements.txt`, install from it:

```powershell
pip install -r requirements.txt
```

If `requirements.txt` is not present, install Django (the project was developed with Django 5.x):

```powershell
pip install django
```

3. Apply migrations

```powershell
python manage.py migrate
```

4. (Optional) Create a superuser to access the admin panel

```powershell
python manage.py createsuperuser
```

5. Run the development server

```powershell
python manage.py runserver
```

Open http://127.0.0.1:8000/ in your browser to view the app. The admin panel is available at `/admin/`.

## Usage notes

- The main template is `templates/home.html`. Edit this file to change the UI.
- Project settings live in `todo_project/settings.py` (database, middleware, installed apps).

## Development & testing

- There are currently no automated tests included. To add tests, create a `tests.py` inside your app or a `tests/` package and run `python manage.py test`.
- Linting/formatting: use your preferred tools (flake8/black).

## Contributing

1. Fork the repo and create a feature branch.
2. Make your changes and run the app locally to verify behavior.
3. Open a pull request with a clear description of your changes.

If you'd like help adding features (user accounts, persistent priorities, REST API, etc.), open an issue describing what you'd like.

## Troubleshooting

- If the server fails to start because of port conflicts, run `python manage.py runserver 8001` (or another port).
- If database errors appear, try removing `db.sqlite3` and re-running migrations (only if you don't need existing data):

```powershell
Remove-Item .\db.sqlite3
python manage.py migrate
```

## License

No license is specified in this repository. If you wish to open-source this project, add a `LICENSE` file (for example MIT) at the repo root.

## About / Contact

Repository owner: `Arnav10090` (GitHub). For further details or to request changes to this README, open an issue or create a pull request.

---

If you'd like, I can also:

- add a `requirements.txt` generated from the included `env` packages,
- add a short CONTRIBUTING.md or LICENSE file,
- or open a PR that adds basic tests or CI.

Tell me which of those you'd like next.
