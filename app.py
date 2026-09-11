import os
from dotenv import load_dotenv

load_dotenv()
from flask import Flask, render_template, request, redirect, url_for,flash
import mysql.connector

app = Flask(__name__)
app.secret_key = os.getenv("SECRET_KEY")

def get_db_connection():
    return mysql.connector.connect(
        host=os.getenv("DB_HOST"),
        user=os.getenv("DB_USER"),
        password=os.getenv("DB_PASSWORD"),
        database=os.getenv("DB_NAME")
    )

@app.route("/")
def home():

    search = request.args.get("search", "")
    status = request.args.get("status", "")

    connection = get_db_connection()
    cursor = connection.cursor(dictionary=True)

    query = "SELECT * FROM tasks WHERE 1=1"
    values = []

    if search:
        query += " AND task LIKE %s"
        values.append("%" + search + "%")

    if status:
        query += " AND status=%s"
        values.append(status)

    cursor.execute(query, values)

    tasks = cursor.fetchall()

    cursor.close()
    connection.close()

    return render_template(
        "index.html",
        tasks=tasks,
        search=search,
        status=status
    )

@app.route("/add-task", methods=["GET", "POST"])
def add_task():

    if request.method == "POST":

        task = request.form["task"].strip()

        if not task:
            flash("Task cannot be empty!", "error")
            return redirect(url_for("add_task"))  
        connection = get_db_connection()
        cursor = connection.cursor()

        cursor.execute(
            "INSERT INTO tasks (task) VALUES (%s)",
            (task,)
        )

        connection.commit()

        cursor.close()
        connection.close()

        flash("Task added successfully!", "success")
        return redirect(url_for("home"))

    return render_template("add_task.html")

@app.route("/delete-task/<int:id>")
def delete_task(id):

    connection = get_db_connection()
    cursor = connection.cursor()

    cursor.execute(
        "DELETE FROM tasks WHERE id=%s",
        (id,)
    )

    connection.commit()

    cursor.close()
    connection.close()

    flash("Task deleted successfully!", "success")

    return redirect(url_for("home"))

@app.route("/complete-task/<int:id>")
def complete_task(id):

    connection = get_db_connection()
    cursor = connection.cursor()

    cursor.execute(
        "UPDATE tasks SET status=%s WHERE id=%s",
        ("Completed", id)
    )

    connection.commit()

    cursor.close()
    connection.close()

    flash("Task completed successfully!", "success")

    return redirect(url_for("home"))

@app.route("/edit-task/<int:id>", methods=["GET", "POST"])
def edit_task(id):

    connection = get_db_connection()
    cursor = connection.cursor(dictionary=True)

    if request.method == "POST":

        new_task = request.form["task"].strip()

        if not new_task:
            flash("Task cannot be empty!", "error")
            return redirect(url_for("edit_task", id=id))

        cursor.execute(
            "UPDATE tasks SET task=%s WHERE id=%s",
            (new_task, id)
        )

        connection.commit()

        cursor.close()
        connection.close()

        flash("Task updated successfully!", "success")

        return redirect(url_for("home"))

    cursor.execute(
        "SELECT * FROM tasks WHERE id=%s",
        (id,)
    )

    task = cursor.fetchone()

    cursor.close()
    connection.close()

    return render_template("edit_task.html", task=task)


if __name__ == "__main__":
    app.run(debug=True)