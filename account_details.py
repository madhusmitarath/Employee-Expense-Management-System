import sqlite3
from tkinter import *

def back(v,c):
	v.deiconify()
	c.destroy()
	
def account_details(root,root1):
        i=3
        conn=sqlite3.connect("database.db")
        p=conn.cursor()
        p.execute("select * from applyvoucher order by expense_date;")
        result=p.fetchall()

        e=Toplevel(root)
        e.title("account details")
        e.minsize(1250,700)
        e.configure(background="snow")
	
    
        lt1=Label(e,font="Bold 15",bg="snow",fg="black",text="Username : ").grid(row=0,column=0)
        lt2=Label(e,font="Bold 15",bg="snow",fg="black",text="Designation : ").grid(row=0,column=1)
        lt3=Label(e,font="Bold 15",bg="snow",fg="black",text="ExpenseDate  : ").grid(row=0,column=2)
        lt4=Label(e,font="Bold 15",bg="snow",fg="black",text="ExpensePurpose: ").grid(row=0,column=3)
        lt5=Label(e,font="Bold 15",bg="snow",fg="black",text="Voucher : ").grid(row=0,column=4)
        lt6=Label(e,font="Bold 15",bg="snow",fg="black",text="Payment : ").grid(row=0,column=5)
        lt7=Label(e,font="Bold 15",bg="snow",fg="black",text="Status : ").grid(row=0,column=6)

        for username,designation,expense_date,expense_purpose,voucher,payment,status in result:
                l1=Label(e,font="Bold 15",bg="snow",fg="blue4",text=username).grid(row=i,column=0)
                l2=Label(e,font="Bold 15",bg="snow",fg="blue4",text=designation).grid(row=i,column=1)
                l3=Label(e,font="Bold 15",bg="snow",fg="blue4",text=expense_date).grid(row=i,column=2)
                l4=Label(e,font="Bold 15",bg="snow",fg="blue4",text=expense_purpose).grid(row=i,column=3)
                l5=Label(e,font="Bold 15",bg="snow",fg="blue4",text=voucher).grid(row=i,column=4)
                l6=Label(e,font="Bold 15",bg="snow",fg="blue4",text=payment).grid(row=i,column=5)
                l7=Label(e,font="Bold 15",bg="snow",fg="blue4",text=status).grid(row=i,column=6)
                i+=1
        b4=Button(e, bg="firebrick4",fg="white", text='Back',font="Bold 10",pady=3.0,relief = RAISED,height=1,width=15,command= lambda : back(root,e))
        b4.place(x=500, y=500)
        root.withdraw()
        root1.withdraw
        e.mainloop()
        return e
