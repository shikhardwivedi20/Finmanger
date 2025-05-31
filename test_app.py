from auth import register_user, login_user
from db import get_connection


def test_register_user():
    username = "testuser1"
    password = "testpass"

    # Clean previous test data
    with get_connection() as conn:
        conn.execute("DELETE FROM users WHERE username = ?", (username,))
        conn.commit()

    assert register_user(username, password) is True

def test_login_success():
    user_id = login_user("testuser1", "testpass")
    assert user_id is not None

def test_add_transaction():
    from finance import add_transaction
    user_id = login_user("testuser1", "testpass")
    assert user_id is not None

    with get_connection() as conn:
        conn.execute('''
            INSERT INTO transactions (user_id, type, category, amount, date)
            VALUES (?, ?, ?, ?, DATE('now'))
        ''', (user_id, 'expense', 'Test', 100))
        conn.commit()

        cursor = conn.cursor()
        cursor.execute("SELECT * FROM transactions WHERE user_id = ? AND category = 'Test'", (user_id,))
        txn = cursor.fetchone()
        assert txn is not None
