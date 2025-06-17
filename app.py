from flask import Flask, render_template, request, redirect, session
import sqlite3

app = Flask(__name__)
app.secret_key = "secret123"

def get_db():
    conn = sqlite3.connect("database.db")
    return conn

@app.route("/")
def index():
    return render_template("index.html")

@app.route("/register", methods=["GET", "POST"])
def register():
    if request.method == "POST":
        role = request.form["role"]
        name = request.form["name"]
        email = request.form["email"]
        password = request.form["password"]
        conn = get_db()
        cursor = conn.cursor()
        cursor.execute("INSERT INTO users (role, name, email, password) VALUES (?, ?, ?, ?)",
                       (role, name, email, password))
        conn.commit()
        conn.close()
        return redirect("/login")
    return render_template("register.html")

@app.route("/login", methods=["GET", "POST"])
def login():
    if request.method == "POST":
        email = request.form["email"]
        password = request.form["password"]
        conn = get_db()
        cursor = conn.cursor()
        cursor.execute("SELECT * FROM users WHERE email=? AND password=?", (email, password))
        user = cursor.fetchone()
        conn.close()
        if user:
            session["user"] = user
            return redirect("/dashboard")
    return render_template("login.html")

@app.route("/dashboard")
def dashboard():
    if "user" in session:
        user = session["user"]
        if user[1] == "doctor":
            return render_template("doctor_dashboard.html", user=user)
        else:
            return render_template("dashboard.html", user=user)
    return redirect("/login")

if __name__ == "__main__":
    app.run(debug=True)
