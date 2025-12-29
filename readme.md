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

---

## ⚙️ Setup Instructions

Follow the steps below to run the Expense Tracker System on your local machine.

---

### 1️⃣ Prerequisites

Ensure you have the following installed:
- Python 3.x  
- Oracle Database (XE / Local instance running)  
- Oracle SQL Developer (optional, for database management)  

Install the Oracle DB Python driver:

```bash
pip install oracledb

---

## 5️⃣ Use the Menu

You will be presented with a menu-driven interface to:

Add expenses
View expenses
Update expenses
Delete expenses
View monthly summaries

---
