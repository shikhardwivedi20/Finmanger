from getpass import getpass
from db import get_connection


def register():
    username = input("Enter username: ")
    password = getpass("Enter password: ")

    with get_connection() as conn:
        try:
            conn.execute("INSERT INTO users (username, password) VALUES (?, ?)", (username, password))
            conn.commit()
            print("✅ Registration successful!")
        except Exception as e:
            print("❌ Error:", e)


def login():
    username = input("Username: ")
    password = getpass("Password: ")

    with get_connection() as conn:
        cursor = conn.cursor()
        cursor.execute("SELECT * FROM users WHERE username = ? AND password = ?", (username, password))
        user = cursor.fetchone()
        if user:
            print(f"✅ Welcome back, {username}!")
            return user[0]  # return user_id
        else:
            print("❌ Invalid credentials.")
            return None

# 🔧 Helper functions for testing (used in test_app.py)
def register_user(username, password):
    with get_connection() as conn:
        cursor = conn.cursor()
        cursor.execute("SELECT * FROM users WHERE username = ?", (username,))
        if cursor.fetchone():
            return False  # User already exists
        cursor.execute("INSERT INTO users (username, password) VALUES (?, ?)", (username, password))
        conn.commit()
        return True

def login_user(username, password):
    with get_connection() as conn:
        cursor = conn.cursor()
        cursor.execute("SELECT id FROM users WHERE username = ? AND password = ?", (username, password))
        result = cursor.fetchone()
        return result[0] if result else None
