from db import get_connection
from datetime import datetime
from budget import check_budget


def add_transaction(user_id):
    print("1. Income")
    print("2. Expense")
    type_choice = input("Choose type (1/2): ")

    if type_choice == '1':
        type_ = 'income'
    elif type_choice == '2':
        type_ = 'expense'
    else:
        print("❌ Invalid choice.")
        return
    amount = float(input("Amount: "))
    category = input("Category (e.g., Food, Rent, Salary): ")
    description = input("Description (optional): ")
    date = input("Date (YYYY-MM-DD) or leave blank for today: ") or datetime.now().strftime("%Y-%m-%d")

    with get_connection() as conn:
        conn.execute('''
            INSERT INTO transactions (user_id, type, amount, category, description, date)
            VALUES (?, ?, ?, ?, ?, ?)
        ''', (user_id, type_, amount, category, description, date))
        conn.commit()
        print("✅ Transaction added successfully!")

        # 🔔 Budget check for expense type
    if type_ == 'expense':
        check_budget(user_id, category, amount, date)

def view_transactions(user_id):
    with get_connection() as conn:
        cursor = conn.cursor()
        cursor.execute('''
            SELECT id, type, amount, category, description, date
            FROM transactions
            WHERE user_id = ?
            ORDER BY date DESC
        ''', (user_id,))
        rows = cursor.fetchall()
        print("\n📄 Your Transactions:")
        for row in rows:
            print(f"ID: {row[0]}, {row[1].capitalize()}, ₹{row[2]} | {row[3]} | {row[4]} | {row[5]}")

def delete_transaction(user_id):
    view_transactions(user_id)
    trans_id = input("Enter ID of transaction to delete: ")
    with get_connection() as conn:
        conn.execute('DELETE FROM transactions WHERE id = ? AND user_id = ?', (trans_id, user_id))
        conn.commit()
        print("🗑️ Transaction deleted.")

def update_transaction(user_id):
    view_transactions(user_id)
    trans_id = input("Enter ID of transaction to update: ")
    amount = float(input("New Amount: "))
    category = input("New Category: ")
    description = input("New Description: ")
    date = input("New Date (YYYY-MM-DD): ")

    with get_connection() as conn:
        conn.execute('''
            UPDATE transactions
            SET amount = ?, category = ?, description = ?, date = ?
            WHERE id = ? AND user_id = ?
        ''', (amount, category, description, date, trans_id, user_id))
        conn.commit()
        print("🔄 Transaction updated.")

