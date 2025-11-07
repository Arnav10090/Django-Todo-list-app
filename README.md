# ✅ Django Todo List App

<div align="center">

![Django](https://img.shields.io/badge/Django-5.2.7-092E20?style=for-the-badge&logo=django&logoColor=white)
![Python](https://img.shields.io/badge/Python-3.x-3776AB?style=for-the-badge&logo=python&logoColor=white)
![SQLite](https://img.shields.io/badge/SQLite-Database-003B57?style=for-the-badge&logo=sqlite&logoColor=white)
![License](https://img.shields.io/badge/License-MIT-green?style=for-the-badge)

**A sleek and intuitive task management application built with Django** 🚀

[Features](#-features) • [Installation](#-installation) • [Usage](#-usage) • [Project Structure](#-project-structure) • [Contributing](#-contributing)

</div>

---

## 📋 Overview

Stay organized and boost your productivity with this elegant Django-powered Todo List application. Manage your daily tasks effortlessly with a clean, user-friendly interface that lets you add, edit, complete, and delete tasks with ease.

## ✨ Features

- ➕ **Add Tasks** - Quickly create new tasks to stay on top of your to-do list
- ✏️ **Edit Tasks** - Update task descriptions anytime
- ✅ **Mark Complete/Incomplete** - Track your progress by toggling task status
- 🗑️ **Delete Tasks** - Remove completed or unwanted tasks
- 📊 **Task Tracking** - Automatic timestamps for task creation and updates
- 🎨 **Clean UI** - Simple and intuitive user interface
- 💾 **SQLite Database** - Lightweight and efficient data storage

## 🛠️ Tech Stack

- **Backend Framework:** Django 5.2.7
- **Database:** SQLite3
- **Language:** Python 3.x
- **Frontend:** HTML Templates

## 📦 Installation

### Prerequisites

- Python 3.x installed on your system
- pip (Python package manager)

### Setup Steps

1. **Clone the repository**
   ```bash
   git clone https://github.com/yourusername/django-todo-list.git
   cd django-todo-list
   ```

2. **Create a virtual environment**
   ```bash
   python -m venv env
   ```

3. **Activate the virtual environment**
   - Windows:
     ```bash
     env\Scripts\activate
     ```
   - macOS/Linux:
     ```bash
     source env/bin/activate
     ```

4. **Install dependencies**
   ```bash
   pip install django
   ```

5. **Run migrations**
   ```bash
   python manage.py migrate
   ```

6. **Create a superuser (optional)**
   ```bash
   python manage.py createsuperuser
   ```

7. **Start the development server**
   ```bash
   python manage.py runserver
   ```

8. **Access the application**
   
   Open your browser and navigate to: `http://127.0.0.1:8000/`

## 📁 Project Structure

```
django-todo-list/
├── todo/                      # Main app directory
│   ├── migrations/           # Database migrations
│   ├── models.py            # Task model definition
│   ├── views.py             # View functions
│   ├── urls.py              # URL routing
│   └── admin.py             # Admin configuration
├── todo_project/             # Project settings
│   ├── settings.py          # Django settings
│   ├── urls.py              # Main URL configuration
│   └── wsgi.py              # WSGI configuration
├── templates/                # HTML templates
│   ├── home.html            # Main task list view
│   └── edit_task.html       # Task editing view
├── db.sqlite3               # SQLite database
└── manage.py                # Django management script
```

## 👨‍💻 Author

**Your Name**

- GitHub: [@Arnav10090](https://github.com/Arnav10090)
- Project: [Django-Todo-list-app](https://github.com/Arnav10090/Django-Todo-list-app)

<div align="center">

**⭐ Star this repository if you find it helpful!**

Made with ❤️ using Django

</div>
