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
    
def view_expenses(cur):
    try:
        cur.execute("SELECT * FROM EXPENSES")
        rows=cur.fetchall()

        if not rows:
            print("No Data found.")
            return
        
        else:
            print("\n-----ALL EXPENSES LIST-----")
            for i in rows:
                print("ID: ",i[0])
                print("Cost: Rs. ",i[1])
                print("Category: ",i[2])
                print("Note: ",i[3])
                print("Date of Expenditure: ",i[4])
                print("-------------------------------------\n")

    except Exception as e:
        print("An error occured while displaying the data: ",e)