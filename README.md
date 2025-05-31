
# 💸 Personal Finance Management Application (FinManager)

A command-line Python application to help users manage their personal finances by tracking income, expenses, setting budgets, and generating insightful reports. Developed using `SQLite3` for persistent data storage and `pytest` for testing.

---

## 📁 Project Structure

```
Finmanager/
├── auth.py             # User registration and login (with testing support)
├── budget.py           # Budget setting and budget limit alert logic
├── db.py               # Database setup and connection utility
├── finance.py          # Income and expense transaction handling
├── FinManager.db       # Maintains the database
├── main.py             # Application entry point and CLI menu
├── reports.py          # Monthly and yearly financial reporting
├── backup_restore.py   # Data backup and restore functionality (optional)
├── test_app.py         # Unit tests using pytest
```

---

## 🚀 Features

### 🔐 User Authentication
- User registration with unique usernames
- Secure login functionality

### 💰 Income & Expense Tracking
- Add, view, and delete transactions
- Categories like Food, Rent, Salary, etc.

### 📊 Financial Reports
- Monthly and yearly summaries
- Displays total income, expenses, and savings

### 📉 Budgeting
- Set monthly budgets for different categories
- Alert when expenses exceed budget limit

### 💾 Data Persistence
- Data stored using SQLite3
- Backup and restore support (optional)

### 🧪 Testing
- `pytest`-based tests for user registration, login, and transactions

---

## 🖥 How to Run the Application

### ✅ Prerequisites
- Python 3.8+
- PIP (Python Package Installer)

### 🛠 Installation

1. **Clone the Repository**  
   ```bash
   git clone https://github.com/shikhardwivedi20/Finmanager.git
   cd Finmanager
   ```

2. **Create Virtual Environment**  
   ```bash
   python -m venv venv
   source venv/bin/activate  # For Unix/Mac
   venv\Scripts\activate     # For Windows
   ```

3. **Install Required Packages**
   ```bash
   pip install -r requirements.txt
   ```

> If `requirements.txt` is missing, just install manually:
```bash
pip install pytest
```

---

## ▶️ Running the App

Run the main program:

```bash
python main.py
```

You’ll be greeted with a CLI menu to:
- Register or login
- Add/view/delete transactions
- Generate reports
- Set budget
- Backup/restore data

---

## 🧪 Running Tests

To run automated unit tests:

```bash
pytest test_app.py
```

You should see:

```
============================== 4 passed in 0.20s ==============================
```

---

## 📦 Sample SQLite Tables Used

### `users`
| id | username  | password |
|----|-----------|----------|

### `transactions`
| id | user_id | type   | category | amount | date       |
|----|---------|--------|----------|--------|------------|

### `budgets`
| id | user_id | category | amount | month | year |
|----|---------|----------|--------|-------|------|

---

## 👨‍💻 Author

Developed by **SHIKHAR DWIVEDI**

---

## 📌 Notes
- All data is stored locally using SQLite.
- No internet required for operation.
- Supports testing and future extensibility.
