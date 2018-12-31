import sqlite3
from tkinter import *
import login
import employee
import manager

def back(v,c):
	v.deiconify()
	c.destroy()
	
def total_approved(root,root1):
        #print(name)
        i=3
        conn=sqlite3.connect("database.db")
        p=conn.cursor()
        p.execute("select * from applyvoucher where status ='Approved'order by expense_date;")
        result=p.fetchall()
        #print(result)
        '''for row in result:
                        print(row[0],end=', ')
                        print(row[1],end=', ')
                        print(row[2],end=', ')
                        print(row[3],end=', ')
                        print(row[4],end=', ')
                        print(row[5])'''

        e=Toplevel(root)
        e.title("total approved")
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
        b1=Button(e,bg="Firebrick4",fg="White",width=15,height=1,relief=FLAT,text="Back",font="Bold 15",command=lambda : back(root,e))
        #b2=Button(n, bg="MAROON",fg="WHITE", text='HOME',font="Bold 10",pady=3.0,relief = FLAT,height=1,width=15,command=lambda : home(root,n))'''
        
        i1=Label(e,width=10,height=1,bg="snow",text="").grid(row=i+1,column=0)
        i2=Label(e,width=10,height=2,bg="snow",text="").grid(row=i+1,column=1)
        i3=Label(e,width=10,height=3,bg="snow",text="").grid(row=i+1,column=2)
        i4=Label(e,width=10,height=4,bg="snow",text="").grid(row=i+1,column=3)
        i5=Label(e,width=10,height=5,bg="snow",text="").grid(row=i+1,column=4)
        i6=Label(e,width=10,height=6,bg="snow",text="").grid(row=i+1,column=5)
        i7=Label(e,width=10,height=6,bg="snow",text="").grid(row=i+1,column=6)
	#l.grid(row=0,column=1)
	#t1.pack()
        #b1.grid(row=i+1,column=1)
        #b2.grid(row=i+1,column=2)
        b1.place(x=550,y=500)
        root.withdraw()
        root1.withdraw
        e.mainloop()
        return e
