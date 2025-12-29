# Expense Tracker System (Python + Oracle DB)

A **menu-driven expense tracker application** built using **Python** and **Oracle Database**.  
This project implements full **CRUD operations**, proper **date handling**, and **monthly expense summaries**, demonstrating backend development fundamentals with real database integration.

---

## 🚀 Features

- Add new expenses with date validation  
- View all recorded expenses  
- Update existing expense details (cost, category, note, date)  
- Delete expenses by ID  
- View **monthly expense summary**  
- Oracle `DATE` handling using `TO_DATE`  
- Secure SQL using **bind variables**  
- Clean menu-driven console interface  

---

## 🛠️ Tech Stack

- **Language:** Python  
- **Database:** Oracle Database (XE / Local)  
- **Connector:** `oracledb`  
- **Date Handling:** `datetime` module  

---

## 📂 Database Schema

```sql
CREATE TABLE expenses (
    id NUMBER GENERATED ALWAYS AS IDENTITY PRIMARY KEY,
    cost NUMBER(10,2),
    category VARCHAR2(50),
    note VARCHAR2(100),
    expense_date DATE
);

⚙️ Setup Instructions
1️⃣ Prerequisites

Oracle Database running locally

Python 3.x installed

oracledb module installed

pip install oracledb

2️⃣ Update Database Credentials

Edit the connection section in the Python file:

conn = db.connect(
    user="your_username",
    password="your_password",
    dsn="localhost:1521/XEPDB1"
)

3️⃣ Run the Program
python expense_tracker.py

📋 Menu Options
1. Add an expense
2. View all expenses
3. Update an expense
4. Delete an expense
5. Monthly expense summary
6. Exit

📊 Monthly Summary Logic

Uses Oracle’s EXTRACT(MONTH FROM DATE) for accurate filtering:

SELECT *
FROM expenses
WHERE EXTRACT(MONTH FROM expense_date) = :month;


Total expenditure is calculated in Python.

🧠 Concepts Demonstrated

Python functions & exception handling

Oracle DB connectivity

Parameterized SQL queries (SQL Injection safe)

DATE validation & conversion

Transaction management (commit)

Resource handling (cursor.close(), conn.close())

🔮 Possible Enhancements

Year-wise expense summary

Category-wise analytics

User authentication

Flask-based web version

Frontend UI

👨‍💻 Author

Rohit R
B.Sc Computer Science (Data Analytics) Student