import sqlite3

def get_connection():
    return sqlite3.connect("FinManager.db")

def initialize_db():
    with get_connection() as conn:
        cursor = conn.cursor()
        # User Table
        cursor.execute('''
            CREATE TABLE IF NOT EXISTS users (
                id INTEGER PRIMARY KEY AUTOINCREMENT,
                username TEXT UNIQUE,
                password TEXT
            )
        ''')

        # Transactions Table
        cursor.execute('''
            CREATE TABLE IF NOT EXISTS transactions (
                id INTEGER PRIMARY KEY AUTOINCREMENT,
                user_id INTEGER,
                type TEXT,  -- "income" or "expense"
                amount REAL,
                category TEXT,
                description TEXT,
                date TEXT,
                FOREIGN KEY(user_id) REFERENCES users(id)
            )
        ''')

        # Budget Table
        cursor.execute('''
            CREATE TABLE IF NOT EXISTS budgets (
                id INTEGER PRIMARY KEY AUTOINCREMENT,
                user_id INTEGER,
                category TEXT NOT NULL,
                amount REAL NOT NULL,
                month TEXT NOT NULL,  -- Format: YYYY-MM
                FOREIGN KEY (user_id) REFERENCES users(id)
            )
        ''')

        conn.commit()
