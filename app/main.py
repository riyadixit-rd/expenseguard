from fastapi import FastAPI
import sqlite3

app = FastAPI()

@app.post("/login")
def login(user: dict):

    username = user.get("username")
    password = user.get("password")

    conn = sqlite3.connect("expenses.db")
    cursor = conn.cursor()

    cursor.execute(
        "SELECT * FROM users WHERE username=? AND password=?",
        (username, password)
    )

    data = cursor.fetchone()

    conn.close()

    if data:
        return {
            "status": "success",
            "username": username,
            "role": "admin" if username == "admin" else "employee"
        }
    else:
        return {"status": "fail"}