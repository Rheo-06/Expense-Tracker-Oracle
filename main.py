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
        cur.execute("SELECT id FROM expenses WHERE id = :1", (n_id,))
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