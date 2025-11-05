# Django Todo List App

A simple Todo List web application built with Django. This project demonstrates creating, completing, and managing todo items with a clean and user-friendly interface.

## Quick summary

- Framework: Django 5.2.7 (project includes a local `env/` with Django installed)
- Database: SQLite (`db.sqlite3`)
- Frontend: Bootstrap 5.3 with Font Awesome icons

## Features

- Add new todo items with a simple input form
- Mark items as complete with a single click
- View completed tasks in a separate section
- Edit existing tasks
- Delete tasks
- Clean and responsive Bootstrap UI
- Date display showing current day
- Scrollable task lists for better organization

## Tech stack

- Python 3.10+ (recommended)
- Django 5.x (installed in the provided `env`)
- SQLite (built-in with Django; database file `db.sqlite3`)

## Project structure (top-level)

- `manage.py` — Django management script
- `todo_project/` — Django project module (settings, urls, views, wsgi/asgi)
- `todo/` — Main application module containing models, views, and URLs
- `templates/` — HTML templates
  - `home.html` — Main page template with task list and form
  - `edit_task.html` — Template for editing tasks
- `db.sqlite3` — SQLite database used in development
- `env/` — Virtual environment with project dependencies

The application follows a standard Django project structure with the main application logic in the `todo/` directory and templates in the `templates/` directory.

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