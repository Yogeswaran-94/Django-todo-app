# Django To-Do Project

A simple Django-based To-Do list application that lets you add, complete, and delete tasks.

## Features
- Add new tasks
- Mark tasks as completed
- Delete tasks
- Basic Bootstrap UI

## Requirements
- Python 3.11+
- Django 5.x

## Installation

1. **Clone the repository**
```bash
git clone https://github.com/Yogeswaran-94/Django-todo_project.git
cd todo_project
Create and activate a virtual environment
python -m venv venv
venv\Scripts\activate

Install dependencies
pip install -r requirements.txt

Apply migrations
python manage.py migrate

Run the development server
python manage.py runserver

Project link:
http://127.0.0.1:8000/

Project Structure
todo_project/
    manage.py
    todo_project/
        settings.py
        urls.py
    todo_app/
        templates/
            todo_app/
                base.html
                index.html
        static/

License
This project is licensed under the MIT License.

