import oracledb as db
from datetime import datetime 

def add_expenses(conn,cur):
    try:
        c=int(input("Enter the Cost:"))
        cat=input("Enter Category: ")
        note=input("Enter a note: ")
        dt=input("Enter the date of expenditure (dd/mm/yyyy): ")
        datetime.strptime(dt,"%d/%m/%Y")
        
        cur.execute("""INSERT INTO EXPENSES(Cost,Description,Note,Expense_Date) 
                    VALUES(:1,:2,:3,TO_DATE(:4, 'DD/MM/YYYY'))""",(c,cat,note,dt))
        conn.commit()
        print("Expense added successfully!")
    except Exception as e:
        print("An error occured while adding data: ",e)