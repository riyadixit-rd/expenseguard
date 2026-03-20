import sqlite3

DB_NAME = "expenses.db"

def get_connection():
    conn = sqlite3.connect(DB_NAME)
    conn.row_factory = sqlite3.Row
    return conn


def create_tables():
    conn = get_connection()
    cursor = conn.cursor()

    # USERS TABLE
    cursor.execute("""
    CREATE TABLE IF NOT EXISTS users (
        id INTEGER PRIMARY KEY AUTOINCREMENT,
        username TEXT UNIQUE,
        password TEXT,
        role TEXT
    )
    """)

    # EXPENSE TABLE
    cursor.execute("""
    CREATE TABLE IF NOT EXISTS expenses (
        id INTEGER PRIMARY KEY AUTOINCREMENT,
        name TEXT,
        amount REAL,
        category TEXT,
        fraud_score INTEGER,
        status TEXT
    )
    """)

    # DEFAULT ADMIN
    cursor.execute("""
    INSERT OR IGNORE INTO users (username,password,role)
    VALUES ('admin','admin123','admin')
    """)

    # DEFAULT EMPLOYEE
    cursor.execute("""
    INSERT OR IGNORE INTO users (username,password,role)
    VALUES ('riya','riya123','employee')
    """)

    conn.commit()
    conn.close()