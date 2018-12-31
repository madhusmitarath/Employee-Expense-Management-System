import sqlite3
from tkinter import *
import login
import employee
import manager
import admin
import checkstatus

def back(v,c):
	v.deiconify()
	c.destroy()

conn=sqlite3.connect("database.db")
p=conn.cursor()	
def delete_voucher(root,root1,name):
        def store(a):
            print(a)
            if a!='':
                    p.execute("delete from applyvoucher where username='"+name+"' and expense_date ='"+a+"';")
                    conn.commit()
                    messagebox.showinfo("Success","Succesfully Deleted")
                    h.destroy()								#Update the Result 
                    delete_voucher(root,root1,name)							#after delete operation
            else:
                    messagebox.showinfo("ERROR4","Nothing is Selected")
                
        i=3
        p.execute("select * from applyvoucher where username = '"+name+"'order by expense_date;")
        result=p.fetchall()

        h=Toplevel(root)
        h.title("delete voucher")
        h.minsize(1250,700)
        h.configure(background="snow")
        a=StringVar()
        lt7=Label(h,font="Bold 15",fg="black",bg="snow",text="Delete : ").grid(row=0,column=0)
        lt1=Label(h,font="Bold 15",fg="black",bg="snow",text="Username : ").grid(row=0,column=1)
        lt2=Label(h,font="Bold 15",fg="black",bg="snow",text="Designation : ").grid(row=0,column=2)
        lt3=Label(h,font="Bold 15",fg="black",bg="snow",text="ExpenseDate  : ").grid(row=0,column=3)
        lt4=Label(h,font="Bold 15",fg="black",bg="snow",text="ExpensePurpose: ").grid(row=0,column=4)
        lt5=Label(h,font="Bold 15",fg="black",bg="snow",text="Voucher : ").grid(row=0,column=5)
        lt6=Label(h,font="Bold 15",fg="black",bg="snow",text="Payment : ").grid(row=0,column=6)
        #lt7=Label(n,font="Bold 15",fg="BLACK",bg="black",text="Status : ").grid(row=0,column=6)

        for username,designation,expense_date,expense_purpose,voucher,payment,status in result:
                Radiobutton(h,bg="snow",fg="blue4",variable=a,value=expense_date,font=(None,12)).grid(row=i,column=0)
                l1=Label(h,font="Bold 15",fg="blue4",bg="snow",text=username).grid(row=i,column=1)
                l2=Label(h,font="Bold 15",fg="blue4",bg="snow",text=designation).grid(row=i,column=2)
                l3=Label(h,font="Bold 15",fg="blue4",bg="snow",text=expense_date).grid(row=i,column=3)
                l4=Label(h,font="Bold 15",fg="blue4",bg="snow",text=expense_purpose).grid(row=i,column=4)
                l5=Label(h,font="Bold 15",fg="blue4",bg="snow",text=voucher).grid(row=i,column=5)
                l6=Label(h,font="Bold 15",fg="blue4",bg="snow",text=payment).grid(row=i,column=6)
                i+=1
                        
        b1=Button(h,bg="MAROON",fg="WHITE",relief=RAISED,text="BACK",font="Bold 10",height=1,width=10,command=lambda : back(root,h))
        b2=Button(h,bg="DEEP SKY BLUE",fg="BLACK", text='Delete',font="Bold 10",relief = RAISED,height=1,width=10,command=lambda : store(a.get()))



	#l.grid(row=0,column=1)
	#t1.pack()
        b1.place(x=300, y=500)
        b2.place(x=600 ,y=500)
        #b2.grid(row=i+1,column=2)
        #b1.place(anchor=S)
        root.withdraw()
        root1.withdraw
        h.mainloop()
        return h
