import sqlite3
from fastapi import FastAPI, Request
from fastapi.middleware.cors import CORSMiddleware

app = FastAPI()

# Allow frontend access
app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

DB = "expenses.db"

# ======================
# DATABASE INIT
# ======================

def init_db():

    conn = sqlite3.connect(DB)
    cursor = conn.cursor()

    # USERS TABLE
    cursor.execute("""
    CREATE TABLE IF NOT EXISTS users(
        id INTEGER PRIMARY KEY AUTOINCREMENT,
        username TEXT UNIQUE,
        password TEXT
    )
    """)

    # EXPENSES TABLE
    cursor.execute("""
    CREATE TABLE IF NOT EXISTS expenses(
        id INTEGER PRIMARY KEY AUTOINCREMENT,
        name TEXT,
        amount INTEGER,
        category TEXT,
        score INTEGER,
        status TEXT
    )
    """)

    # INSERT DEFAULT ADMIN (only once)
    cursor.execute("""
    INSERT OR IGNORE INTO users(username,password)
    VALUES('admin','admin123')
    """)

    conn.commit()
    conn.close()

# run at startup
init_db()

# ======================
# LOGIN API
# ======================

@app.post("/login")
async def login(request: Request):

    data = await request.json()

    username = data.get("username")
    password = data.get("password")

    conn = sqlite3.connect(DB)
    cursor = conn.cursor()

    cursor.execute(
        "SELECT * FROM users WHERE username=? AND password=?",
        (username, password)
    )

    user = cursor.fetchone()
    conn.close()

    if user:
        return {
            "status": "success",
            "username": username
        }

    return {"status": "fail"}

# ======================
# ADD EMPLOYEE
# ======================

@app.post("/add_employee")
async def add_employee(request: Request):

    data = await request.json()

    username = data.get("username")
    password = data.get("password")

    conn = sqlite3.connect(DB)
    cursor = conn.cursor()

    try:
        cursor.execute(
            "INSERT INTO users(username,password) VALUES(?,?)",
            (username, password)
        )
        conn.commit()
    except:
        pass

    conn.close()

    return {"status": "success"}

# ======================
# GET EMPLOYEES
# ======================

@app.get("/employees")
def get_employees():

    conn = sqlite3.connect(DB)
    conn.row_factory = sqlite3.Row
    cursor = conn.cursor()

    data = cursor.execute(
        "SELECT username FROM users"
    ).fetchall()

    conn.close()

    return [dict(row) for row in data]

# ======================
# FRAUD DETECTION
# ======================

def detect_fraud(amount, category):

    score = 0

    if amount > 30000:
        score += 50

    if category == "Travel":
        score += 30

    if category == "Hotel":
        score += 20

    status = "Fraud" if score >= 50 else "Safe"

    return score, status

# ======================
# ADD EXPENSE
# ======================

@app.post("/add_expense")
async def add_expense(request: Request):

    data = await request.json()

    name = data.get("name")
    amount = int(data.get("amount"))
    category = data.get("category")

    score, status = detect_fraud(amount, category)

    conn = sqlite3.connect(DB)
    cursor = conn.cursor()

    cursor.execute("""
    INSERT INTO expenses(name,amount,category,score,status)
    VALUES(?,?,?,?,?)
    """, (name, amount, category, score, status))

    conn.commit()
    conn.close()

    return {
        "status": status,
        "score": score
    }

# ======================
# GET EXPENSES
# ======================

@app.get("/expenses")
def get_expenses():

    conn = sqlite3.connect(DB)
    conn.row_factory = sqlite3.Row
    cursor = conn.cursor()

    data = cursor.execute(
        "SELECT * FROM expenses"
    ).fetchall()

    conn.close()

    return [dict(row) for row in data]