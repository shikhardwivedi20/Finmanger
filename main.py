from db import initialize_db
from auth import register, login
from finance import add_transaction, view_transactions, delete_transaction, update_transaction
from budget import set_budget
from reports import generate_report
from backup_restore import backup_database, restore_database



def finance_menu(user_id):
    while True:
        print("\n📊 Finance Menu:")
        print("1. Add Transaction")
        print("2. View Transactions")
        print("3. Update Transaction")
        print("4. Delete Transaction")
        print("5. Generate Financial Report")
        print("6. Set Monthly Budget")
        print("7. Backup Database")
        print("8. Restore Database")
        print("9. Logout")

        choice = input("Choose an option: ")

        if choice == '1':
            add_transaction(user_id)
        elif choice == '2':
            view_transactions(user_id)
        elif choice == '3':
            update_transaction(user_id)
        elif choice == '4':
            delete_transaction(user_id)
        elif choice == '5':
            generate_report(user_id)
        elif choice == '6':
            set_budget(user_id)
        elif choice == '7':
            backup_database()
        elif choice == '8':
            restore_database()
        elif choice == '9':
            print("👋 Logged out.")
            break
        else:
            print("Invalid choice.")


def main():
    initialize_db()
    print("📊 Welcome to FinManager 📊")

    while True:
        print("\n1. Register\n2. Login\n3. Exit")
        choice = input("Choose an option: ")

        if choice == '1':
            register()
        elif choice == '2':
            user_id = login()
            if user_id:
                finance_menu(user_id)
        elif choice == '3':
            print("Goodbye!")
            break
        else:
            print("Invalid choice!")

if __name__ == "__main__":
    main()
