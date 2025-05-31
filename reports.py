from db import get_connection
from datetime import datetime
import calendar

def generate_report(user_id):
    print("\n📅 Report Options:")
    print("1. Monthly Report")
    print("2. Yearly Report")
    choice = input("Choose an option: ")

    if choice == '1':
        month = input("Enter month (01 to 12): ")
        year = input("Enter year (e.g. 2025): ")
        try:
            # Calculate last day of the selected month
            last_day = calendar.monthrange(int(year), int(month))[1]
            start = f"{year}-{month}-01"
            end = f"{year}-{month}-{last_day}"
        except Exception as e:
            print("❌ Invalid month/year input.")
            return
    elif choice == '2':
        year = input("Enter year (e.g. 2025): ")
        start = f"{year}-01-01"
        end = f"{year}-12-31"
    else:
        print("❌ Invalid choice.")
        return

    with get_connection() as conn:
        cursor = conn.cursor()
        cursor.execute('''
            SELECT type, SUM(amount)
            FROM transactions
            WHERE user_id = ? AND date BETWEEN ? AND ?
            GROUP BY type
        ''', (user_id, start, end))
        results = cursor.fetchall()

    income = 0
    expense = 0

    for type_, amount in results:
        if type_ == 'income':
            income = amount
        elif type_ == 'expense':
            expense = amount

    savings = income - expense

    print("\n📈 Financial Summary:")
    print(f"🟢 Total Income: ₹{income:.2f}")
    print(f"🔴 Total Expenses: ₹{expense:.2f}")
    print(f"💰 Savings: ₹{savings:.2f}")
