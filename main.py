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
        print("An error occurred while adding data: ",e)
    
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
        print("An error occurred while displaying the data: ",e)

def update_expenses(conn,cur):
    try:
        n_id=int(input("Enter the expense ID to update: "))
        cur.execute("SELECT id FROM EXPENSES WHERE id = :1", (n_id,))
        if cur.fetchone() is None:
            print("No expense found with that ID.")
            return
        
        u_type=input("What would you like to update? (Cost/Category/Note/Date): ").lower()
        if u_type=='cost':
            c=float(input("Enter new cost: "))
            cur.execute("""UPDATE EXPENSES SET COST=:1 WHERE ID=:2""",(c,n_id))
        elif u_type=='category':
            cat=input("Enter new Category: ")
            cur.execute("""UPDATE EXPENSES SET CATEGORY=:1 WHERE ID=:2""",(cat,n_id))
        elif u_type=='note':
            n=input("Enter new note: ")
            cur.execute("""UPDATE EXPENSES SET NOTE=:1 WHERE ID=:2""",(n,n_id))
        elif u_type=='date':
            d=input("Enter new Date (dd/mm/yyyy): ")
            datetime.strptime(d,'%d/%m/%Y')
            cur.execute("""UPDATE EXPENSES SET EXPENSE_DATE= TO_DATE(:1,'DD/MM/YYYY')
                            WHERE ID=:2""",(d,n_id))
        else:
            print("Invalid Update option.")

        conn.commit()
        print("Expense Updated Successfully!")

    except Exception as e:
        print("An error occurred wile updating: ",e)

def delete_expenses(conn,cur):
    try:
        n_id=int(input("Enter the expense ID to delete: "))
        cur.execute("SELECT id FROM EXPENSES WHERE id = :1", (n_id,))
        if cur.fetchone() is None:
            print("No expense found with that ID.")
            return
        
        cur.execute("DELETE FROM EXPENSES WHERE ID=:1",(n_id,))
        conn.commit()
        print("Expense Deleted Successfully!")
    except Exception as e:
        print("An error occurred while deletion: ",e)

def summary_expenses(cur):
    try:
        m=int(input("Enter a month to view the summary (1/2/.../11/12): "))
        cur.execute("SELECT * FROM EXPENSES WHERE EXTRACT(MONTH FROM EXPENSE_DATE)=:1",(m,))
        rows=cur.fetchall()
        if not rows:
            print("No Data found.")
            return 
        
        print("\n-------EXPENSE SUMMARY-------\n")
        t=0
        for i in rows:
            print("ID: ",i[0])
            print("Cost: Rs. ",i[1])
            print("Category: ",i[2])
            print("Note: ",i[3])
            print("Date of Expenditure: ",i[4])
            t+=i[1]
        print("Total Expenditude for the month = Rs. ",t)
        print("-------------------------------------\n")

    except Exception as e:
        print("An eroor occurred while loading the summary: ",e)

try:
    conn=db.connect(user='rohit',password='rohit123',dsn='localhost:1521/XEPDB1')
    print("Connection Established Successfully!\n")
    cur=conn.cursor()

    while True:
        print('\n--------WELCOME TO EXPENSE TRACKER SYSTEM--------\n')
        print("Enter 1 for adding an expense.")
        print("Enter 2 for viewing all expenses.")
        print("Enter 3 for updating an expense.")
        print("Enter 4 for deleting an expense.")
        print("Enter 5 to view a detailed monthly summary of expenditure.")
        print("Enter 6 to exit the program.")
        c=int(input("Enter your choice: "))

        if c==1:
            add_expenses(conn,cur)

        elif c==2:
            view_expenses(cur)

        elif c==3:
            update_expenses(conn,cur)

        elif c==4:
            delete_expenses(conn,cur)

        elif c==5:
            summary_expenses(cur)

        elif c==6:
            print("\nExiting the program....")
            break

        else:
            print("Invalid chocie, try again!")

except db.DatabaseError as de:
    print("Couldn't establish connection: ",de)
except Exception as e:
    print("An error occured: ",e)
finally:
    try:
        cur.close()
        conn.close()
        print("Database connection closed.")
    except:
        pass