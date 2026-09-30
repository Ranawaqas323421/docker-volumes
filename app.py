from flask import Flask, render_template, request, redirect, url_for, flash
from database import get_db_connection, init_db

app = Flask(__name__)
app.secret_key = "task-manager-secret-key"

init_db()


@app.route("/")
def index():
    search = request.args.get("search", "").strip()
    category = request.args.get("category", "")
    priority = request.args.get("priority", "")
    status = request.args.get("status", "")

    connection = get_db_connection()

    query = "SELECT * FROM tasks WHERE 1=1"
    parameters = []

    if search:
        query += " AND (title LIKE ? OR description LIKE ?)"
        parameters.extend([f"%{search}%", f"%{search}%"])

    if category:
        query += " AND category = ?"
        parameters.append(category)

    if priority:
        query += " AND priority = ?"
        parameters.append(priority)

    if status:
        query += " AND status = ?"
        parameters.append(status)

    query += """
        ORDER BY
            CASE priority
                WHEN 'High' THEN 1
                WHEN 'Medium' THEN 2
                WHEN 'Low' THEN 3
            END,
            id DESC
    """

    tasks = connection.execute(query, parameters).fetchall()
    total = connection.execute("SELECT COUNT(*) FROM tasks").fetchone()[0]
    completed = connection.execute(
        "SELECT COUNT(*) FROM tasks WHERE status = 'Completed'"
    ).fetchone()[0]
    pending = connection.execute(
        "SELECT COUNT(*) FROM tasks WHERE status = 'Pending'"
    ).fetchone()[0]
    high_priority = connection.execute(
        "SELECT COUNT(*) FROM tasks WHERE priority = 'High' AND status = 'Pending'"
    ).fetchone()[0]

    connection.close()

    return render_template(
        "index.html",
        tasks=tasks,
        total=total,
        completed=completed,
        pending=pending,
        high_priority=high_priority,
        search=search,
        category=category,
        priority=priority,
        status=status
    )


@app.route("/add", methods=["GET", "POST"])
def add_task():
    if request.method == "POST":
        title = request.form.get("title", "").strip()
        description = request.form.get("description", "").strip()
        category = request.form.get("category", "Personal")
        priority = request.form.get("priority", "Medium")
        due_date = request.form.get("due_date", "")

        if not title:
            flash("Task title is required.", "error")
            return render_template("add_task.html")

        connection = get_db_connection()
        connection.execute(
            """
            INSERT INTO tasks
            (title, description, category, priority, due_date)
            VALUES (?, ?, ?, ?, ?)
            """,
            (title, description, category, priority, due_date)
        )
        connection.commit()
        connection.close()

        flash("Task added successfully.", "success")
        return redirect(url_for("index"))

    return render_template("add_task.html")


@app.route("/edit/<int:task_id>", methods=["GET", "POST"])
def edit_task(task_id):
    connection = get_db_connection()

    task = connection.execute(
        "SELECT * FROM tasks WHERE id = ?",
        (task_id,)
    ).fetchone()

    if task is None:
        connection.close()
        flash("Task not found.", "error")
        return redirect(url_for("index"))

    if request.method == "POST":
        title = request.form.get("title", "").strip()
        description = request.form.get("description", "").strip()
        category = request.form.get("category", "Personal")
        priority = request.form.get("priority", "Medium")
        due_date = request.form.get("due_date", "")
        status = request.form.get("status", "Pending")

        if not title:
            connection.close()
            flash("Task title is required.", "error")
            return render_template("edit_task.html", task=task)

        connection.execute(
            """
            UPDATE tasks
            SET title = ?, description = ?, category = ?,
                priority = ?, due_date = ?, status = ?
            WHERE id = ?
            """,
            (title, description, category, priority, due_date, status, task_id)
        )
        connection.commit()
        connection.close()

        flash("Task updated successfully.", "success")
        return redirect(url_for("index"))

    connection.close()
    return render_template("edit_task.html", task=task)


@app.route("/complete/<int:task_id>")
def complete_task(task_id):
    connection = get_db_connection()
    task = connection.execute(
        "SELECT status FROM tasks WHERE id = ?",
        (task_id,)
    ).fetchone()

    if task:
        new_status = "Pending" if task["status"] == "Completed" else "Completed"
        connection.execute(
            "UPDATE tasks SET status = ? WHERE id = ?",
            (new_status, task_id)
        )
        connection.commit()

    connection.close()
    return redirect(url_for("index"))


@app.route("/delete/<int:task_id>", methods=["POST"])
def delete_task(task_id):
    connection = get_db_connection()
    connection.execute("DELETE FROM tasks WHERE id = ?", (task_id,))
    connection.commit()
    connection.close()

    flash("Task deleted successfully.", "success")
    return redirect(url_for("index"))


if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000, debug=True)
