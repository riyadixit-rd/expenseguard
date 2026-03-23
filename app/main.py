from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
import sqlite3

app = FastAPI()

# CORS (IMPORTANT for frontend)
app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

# LOGIN
@app.post("/login")
def login(data: dict):
    if data["username"] == "admin" and data["password"] == "admin":
        return {"status": "success", "username": "admin", "role": "admin"}
    else:
        return {"status": "success", "username": data["username"], "role": "user"}


# GET EXPENSES
@app.get("/expenses")
def get_expenses():
    conn = sqlite3.connect("expenses.db")
    cursor = conn.cursor()

    cursor.execute("SELECT * FROM expenses")
    data = cursor.fetchall()

    conn.close()

    result = []
    for row in data:
        result.append({
            "id": row[0],
            "name": row[1],
            "amount": row[2],
            "category": row[3],
            "score": row[4],
            "status": row[5]
        })

    return result


# ADD EXPENSE
@app.post("/add_expense")
def add_expense(data: dict):
    name = data["name"]
    amount = int(data["amount"])
    category = data["category"]

    # SIMPLE FRAUD LOGIC
    score = 0
    if amount > 50000:
        score += 80
    elif amount > 20000:
        score += 50

    status = "Fraud" if score > 60 else "Safe"

    conn = sqlite3.connect("expenses.db")
    cursor = conn.cursor()

    cursor.execute("""
    INSERT INTO expenses (name, amount, category, score, status)
    VALUES (?, ?, ?, ?, ?)
    """, (name, amount, category, score, status))

    conn.commit()
    conn.close()

    return {"message": "Expense added"}