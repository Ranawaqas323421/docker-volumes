# 📝 Task Manager – Flask, SQLite & Docker Volumes

A simple and user-friendly **Task Manager web application** built with **Python Flask and SQLite**.

This project was created as a hands-on practice project to understand Flask, database operations, Docker containers, and especially **Docker Volumes for persistent data**.

---

## 🚀 What is this project?

The Task Manager helps you manage your daily tasks from a simple web dashboard.

You can:

- ➕ Add new tasks
- ✏️ Edit existing tasks
- ✅ Mark tasks as completed
- 🗑️ Delete tasks
- 🔍 Search tasks
- 📂 Filter by category
- ⚡ Filter by priority
- 📌 Filter by status
- 📊 View task statistics

The application uses **SQLite** to store task information.

---

## 🖥️ Application Preview

### 📊 Task Dashboard

The dashboard provides a quick overview of your tasks:

- Total Tasks
- Pending Tasks
- Completed Tasks
- High Priority Tasks

It also includes search and filtering options.

![Task Dashboard](screenshot-dashboard.png)

### 🗂️ Empty Dashboard

When there are no tasks, the application displays a simple message and lets you create your first task.

![Empty Task Dashboard](screenshot-empty.png)

---

## ✨ Main Features

### ➕ Add Tasks
Create a task with information such as:

- Title
- Description
- Category
- Priority
- Due date

### ✏️ Edit Tasks
Update task information whenever needed.

### ✅ Complete Tasks
Mark tasks as completed or keep them pending.

### 🔍 Search & Filter
Quickly find tasks using:

- Search
- Category
- Priority
- Status

### 📊 Dashboard
See important task statistics from one place.

---

## 🛠️ Technologies Used

- **Python**
- **Flask**
- **SQLite**
- **HTML**
- **CSS**
- **Jinja2**
- **Docker**
- **Docker Volumes**

---

## 📁 Project Structure

```text
docker-volumes/
│
├── static/
│   └── ...
│
├── templates/
│   ├── index.html
│   ├── add_task.html
│   └── edit_task.html
│
├── app.py
├── database.py
├── requirements.txt
├── tasks.db
└── README.md
```

> The exact files and folders may vary depending on the current version of the project.

---

## ⚙️ Run Locally

### 1. Clone the repository

```bash
git clone https://github.com/Ranawaqas323421/docker-volumes.git
```

### 2. Open the project

```bash
cd docker-volumes
```

### 3. Create a virtual environment

```bash
python3 -m venv venv
```

### 4. Activate it

**Linux/macOS:**

```bash
source venv/bin/activate
```

**Windows:**

```bash
venv\Scripts\activate
```

### 5. Install dependencies

```bash
pip install -r requirements.txt
```

### 6. Start the application

```bash
python3 app.py
```

Then open:

```text
http://localhost:5000
```

---

## 🐳 Docker Volumes

One of the main learning goals of this project is understanding **Docker Volumes**.

A Docker container can be removed and recreated. If application data is stored only inside the container, that data can be lost.

A Docker Volume allows important data to be stored separately from the container.

For example:

```bash
docker volume create task-data
```

A volume can then be mounted into a container:

```bash
docker run -d \
  --name task-manager \
  -p 5000:5000 \
  -v task-data:/app \
  task-manager
```

The exact mount path should match the location used by the application for its persistent data.

### 💡 Simple idea

```text
Flask Application
       ↓
     SQLite
       ↓
 Docker Volume
       ↓
 Persistent Data
```

This means the application data can remain available even when the container itself is recreated, provided the volume is kept.

---

## 🎯 What I Learned

This project helped me practice:

- Flask application development
- SQLite database operations
- CRUD functionality
- Flask routes and forms
- HTML templates
- Search and filtering
- Docker containers
- Docker Volumes
- Persistent application data

---

## 🔮 Future Improvements

Possible future improvements include:

- 🔐 User authentication
- 👥 Multiple users
- 🔔 Task reminders
- 📅 Better date management
- 📈 More dashboard statistics
- 🐳 Improved Docker configuration
- ☁️ AWS/cloud deployment
- 🔄 CI/CD pipeline

---

## 👨‍💻 Author

**Waqas Saleem**

GitHub:  
https://github.com/Ranawaqas323421

---

## ⭐ Support

If you find this project useful for learning, feel free to explore the repository and try it yourself.

Thanks for checking out the project! 🚀
