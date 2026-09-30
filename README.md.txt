# Task Manager

A practical Task Manager web application built with **Python, Flask, SQLite, HTML5, CSS3, and Jinja2**.

## Features

- Create, edit, and delete tasks
- Mark tasks as Completed or Pending
- Search tasks by title or description
- Filter by category, priority, and status
- Set due dates
- Categories: Work, Personal, Study, Other
- Priorities: High, Medium, Low
- Dashboard statistics for total, pending, completed, and high-priority tasks
- Responsive web interface
- SQLite database with automatic initialization

## Technologies Used

- Python 3
- Flask
- SQLite
- HTML5
- CSS3
- Jinja2

## Project Structure

```text
task-manager/
├── app.py
├── database.py
├── requirements.txt
├── templates/
│   ├── base.html
│   ├── index.html
│   ├── add_task.html
│   └── edit_task.html
└── static/
    └── style.css
```

## Installation

Clone the repository:

```bash
git clone YOUR_REPOSITORY_URL
cd task-manager
```

Create a virtual environment:

```bash
python3 -m venv venv
source venv/bin/activate
```

Install dependencies:

```bash
pip install -r requirements.txt
```

## Run the Application

```bash
python3 app.py
```

Open:

```text
http://127.0.0.1:5000
```

For a cloud/server deployment:

```text
http://YOUR_SERVER_IP:5000
```

## Database

This project uses SQLite. The database is initialized automatically when the application starts, and `tasks.db` is created automatically in the project directory.

## Docker

Docker configuration is intentionally not included in this README/project setup so Dockerization can be added separately as part of DevOps practice.

## Future Improvements

- User authentication
- PostgreSQL or MongoDB integration
- REST API
- Docker and Docker Compose
- Nginx reverse proxy
- CI/CD with GitHub Actions
- AWS deployment
- Monitoring and logging

## Author

**Waqas Saleem**
