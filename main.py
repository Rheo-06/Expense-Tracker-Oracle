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
        print("\nExpense added successfully!\n")
    except Exception as e:
        print("\nAn error occurred while adding data: ",e)
    
def view_expenses(cur):
    try:
        cur.execute("SELECT * FROM EXPENSES")
        rows=cur.fetchall()

        if not rows:
            print("\nNo Data found.\n")
            return
        
        else:
            print("\n-----ALL EXPENSES LIST-----\n")
            for i in rows:
                print("ID: ",i[0])
                print("Cost: Rs. ",i[1])
                print("Category: ",i[2])
                print("Note: ",i[3])
                print("Date of Expenditure: ",i[4])
                print("-------------------------------------\n")

    except Exception as e:
        print("\nAn error occurred while displaying the data: ",e)

def update_expenses(conn,cur):
    try:
        n_id=int(input("Enter the expense ID to update: "))
        cur.execute("SELECT id FROM EXPENSES WHERE id = :1", (n_id,))
        if cur.fetchone() is None:
            print("\nNo expense found with that ID.\n")
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
            print("\nInvalid Update option.\n")

        conn.commit()
        print("\nExpense Updated Successfully!\n")

    except Exception as e:
        print("\nAn error occurred wile updating: ",e)

def delete_expenses(conn,cur):
    try:
        n_id=int(input("Enter the expense ID to delete: "))
        cur.execute("SELECT id FROM EXPENSES WHERE id = :1", (n_id,))
        if cur.fetchone() is None:
            print("\nNo expense found with that ID.\n")
            return
        
        cur.execute("DELETE FROM EXPENSES WHERE ID=:1",(n_id,))
        conn.commit()
        print("\nExpense Deleted Successfully!\n")
    except Exception as e:
        print("\nAn error occurred while deletion: ",e)

def summary_expenses(cur):
    try:
        m=int(input("Enter a month to view the summary (1/2/.../11/12): "))
        cur.execute("SELECT * FROM EXPENSES WHERE EXTRACT(MONTH FROM EXPENSE_DATE)=:1",(m,))
        rows=cur.fetchall()
        if not rows:
            print("\nNo Data found.\n")
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
        print("\nAn eroor occurred while loading the summary: ",e)

try:
    conn=db.connect(user='rohit',password='rohit123',dsn='localhost:1521/XEPDB1')
    print("\nConnection Established Successfully!\n")
    cur=conn.cursor()

    print('\n--------WELCOME TO EXPENSE TRACKER SYSTEM--------\n')
    while True:
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
            print("\nExiting the program...\n.")
            break

        else:
            print("\nInvalid chocie, try again!\n")

except db.DatabaseError as de:
    print("\nCouldn't establish connection: ",de)
except Exception as e:
    print("\nAn error occured: ",e)
finally:
    try:
        cur.close()
        conn.close()
        print("Database connection closed.")
    except:
        pass