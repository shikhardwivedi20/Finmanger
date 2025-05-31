from db import get_connection

def set_budget(user_id):
    category = input("Enter category to set budget for (e.g., Food, Rent): ")
    try:
        amount = float(input("Enter monthly budget amount: ₹"))
    except ValueError:
        print("❌ Invalid amount.")
        return
    month = input("Enter month in format YYYY-MM (e.g., 2025-06): ")

    with get_connection() as conn:
        cursor = conn.cursor()
        # Check if budget already exists
        cursor.execute('''
            SELECT id FROM budgets
            WHERE user_id = ? AND category = ? AND month = ?
        ''', (user_id, category, month))
        exists = cursor.fetchone()

        if exists:
            # Update existing budget
            cursor.execute('''
                UPDATE budgets SET amount = ? 
                WHERE user_id = ? AND category = ? AND month = ?
            ''', (amount, user_id, category, month))
            print("🔄 Budget updated.")
        else:
            # Insert new budget
            cursor.execute('''
                INSERT INTO budgets (user_id, category, amount, month)
                VALUES (?, ?, ?, ?)
            ''', (user_id, category, amount, month))
            print("✅ Budget set.")

def check_budget(user_id, category, amount, date):
    if not date:
        return
    month = date[:7]  # Extract YYYY-MM

    with get_connection() as conn:
        cursor = conn.cursor()

        # Get budget amount
        cursor.execute('''
            SELECT amount FROM budgets
            WHERE user_id = ? AND category = ? AND month = ?
        ''', (user_id, category, month))
        row = cursor.fetchone()

        if row:
            budget_limit = row[0]
            # Calculate total expense in that category for the month
            cursor.execute('''
                SELECT SUM(amount) FROM transactions
                WHERE user_id = ? AND type = 'expense' AND category = ? 
                AND strftime('%Y-%m', date) = ?
            ''', (user_id, category, month))
            total_spent = cursor.fetchone()[0] or 0

            if total_spent > budget_limit:
                print(f"⚠️ Budget Exceeded for {category}!")
                print(f"🧾 Budget: ₹{budget_limit:.2f}, Spent: ₹{total_spent:.2f}")

        conn.commit()
