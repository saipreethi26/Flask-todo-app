# Flask To-Do List Application

A web-based To-Do List application developed using **Python Flask, MySQL, HTML, CSS, and Jinja2**. The application allows users to create, view, update, complete, delete, search, and filter tasks.

## 🚀 Features

* Add new tasks
* View all tasks
* Edit tasks
* Delete tasks
* Mark tasks as completed
* Search tasks
* Filter tasks by status
* Success and error flash messages
* Responsive user interface
* MySQL database integration

## 🛠️ Technologies Used

* Python
* Flask
* MySQL
* HTML5
* CSS3
* Jinja2
* mysql-connector-python
* Werkzeug

## 📁 Project Structure

```text
Flask-todo-app/
│
├── app.py
├── requirements.txt
├── .gitignore
├── README.md
│
├── templates/
│   ├── index.html
│   ├── add_task.html
│   └── edit_task.html
│
└── static/
    └── style.css
```

## 🗄️ Database Setup

Create the database:

```sql
CREATE DATABASE todo;
USE todo;
```

Create the tasks table:

```sql
CREATE TABLE tasks (
    id INT PRIMARY KEY AUTO_INCREMENT,
    task VARCHAR(255) NOT NULL,
    status VARCHAR(20) DEFAULT 'Pending'
);
```

## ⚙️ Installation

### 1. Clone the repository

```bash
git clone https://github.com/saipreethi26/Flask-todo-app.git
```

### 2. Open the project

```bash
cd Flask-todo-app
```

### 3. Create a virtual environment

```bash
python -m venv venv
```

### 4. Activate the virtual environment

Windows:

```bash
venv\Scripts\activate
```

### 5. Install the required packages

```bash
pip install -r requirements.txt
```

## 🔧 Database Configuration

Update the MySQL connection details in `app.py` according to your local MySQL setup.

**Do not upload passwords or other sensitive information to GitHub.**

## ▶️ Run the Application

Run:

```bash
python app.py
```

Open your browser and visit:

```text
http://127.0.0.1:5000
```

## 📌 Future Improvements

* User registration and login
* User-specific tasks
* Task due dates
* Task priorities
* Dashboard with task statistics
* REST API
* Cloud deployment

## 👩‍💻 Author

**Saipreethi Gade**

GitHub: https://github.com/saipreethi26
