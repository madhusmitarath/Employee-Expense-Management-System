import sqlite3
from tkinter import *
import login
import employee
import manager
import checkstatus

def back(v,c):
	v.deiconify()
	c.destroy()

conn=sqlite3.connect("database.db")
p=conn.cursor()	
def employee_request(root,root1):
        def store(a,b):
                if a=='' and b == ' ':
                        messagebox.showinfo("ERROR4","Nothing is Selected")
                else:
                        p.execute("select username from applyvoucher")
                        res=p.fetchall()
                        for row in res:
                                if row[0]==a:
                                        p.execute("update applyvoucher set status ='Approved' where username='"+a+"'")
                                        conn.commit()
                                elif row[0]==b:
                                        p.execute("update applyvoucher set status ='Rejected' where username='"+b+"'")
                                        conn.commit()
                        g.destroy()
                        employee_request(root,root1)
                
        #print(name)
        i=3
        result=p.execute("select * from applyvoucher where status='Pending'")
        result=p.fetchall()
        #conn.commit()
        '''for row in result:
                        print(row[0],end=', ')
                        print(row[1],end=', ')
                        print(row[2],end=', ')
                        print(row[3],end=', ')
                        print(row[4],end=', ')
                        print(row[5])'''

        g=Toplevel(root)
        g.title("employee request")
        g.minsize(1250,700)
        g.configure(background="snow")
        a=StringVar()
        b=StringVar()
        lt1=Label(g,font="Bold 15",fg="black",bg="snow",text="Username : ").grid(row=0,column=0)
        lt2=Label(g,font="Bold 15",fg="black",bg="snow",text="Designation : ").grid(row=0,column=1)
        lt3=Label(g,font="Bold 15",fg="black",bg="snow",text="ExpenseDate  : ").grid(row=0,column=2)
        lt4=Label(g,font="Bold 15",fg="black",bg="snow",text="ExpensePurpose: ").grid(row=0,column=3)
        lt5=Label(g,font="Bold 15",fg="black",bg="snow",text="Voucher : ").grid(row=0,column=4)
        lt6=Label(g,font="Bold 15",fg="black",bg="snow",text="Payment : ").grid(row=0,column=5)
        lt7=Label(g,font="Bold 15",fg="black",bg="snow",text="Approve : ").grid(row=0,column=6)
        #lt7=Label(n,font="Bold 15",fg="snow",bg="snow",text="Status : ").grid(row=0,column=6)

        for username,designation,expense_date,expense_purpose,voucher,payment,status in result:
                Radiobutton(g,bg="snow",fg="blue4",variable=a,value=username,text="Yes",font=(None,12)).grid(row=i,column=6)
                l1=Label(g,font="Bold 15",fg="blue4",bg="snow",text=username).grid(row=i,column=0)
                l2=Label(g,font="Bold 15",fg="blue4",bg="snow",text=designation).grid(row=i,column=1)
                l3=Label(g,font="Bold 15",fg="blue4",bg="snow",text=expense_date).grid(row=i,column=2)
                l4=Label(g,font="Bold 15",fg="blue4",bg="snow",text=expense_purpose).grid(row=i,column=3)
                l5=Label(g,font="Bold 15",fg="blue4",bg="snow",text=voucher).grid(row=i,column=4)
                l6=Label(g,font="Bold 15",fg="blue4",bg="snow",text=payment).grid(row=i,column=5)
                i+=1
        i=3        
        for username,designation,expense_date,expense_purpose,voucher,payment,status in result:
                Radiobutton(g,bg="snow",fg="blue4",variable=b,value=username,text="No",font=(None,12)).grid(row=i,column=7)
                i+=1
                        
        b1=Button(g,bg="MAROON",fg="WHITE",relief=RAISED,text="BACK",font="Bold 10",height=1,width=10,command=lambda : back(root,g))
        b2=Button(g,bg="DEEP SKY BLUE",fg="BLACK", text='Update',font="Bold 10",relief = RAISED,height=1,width=10,command=lambda : store(a.get(),b.get()))

        '''i1=Label(g,width=10,height=1,bg="blue4",text="").grid(row=i+1,column=0)
        i2=Label(g,width=10,height=2,bg="blue4",text="").grid(row=i+1,column=1)
        i3=Label(g,width=10,height=3,bg="white",text="").grid(row=i+1,column=2)
        i4=Label(g,width=10,height=4,bg="white",text="").grid(row=i+1,column=3)
        i5=Label(g,width=10,height=5,bg="white",text="").grid(row=i+1,column=4)
        i6=Label(g,width=10,height=6,bg="white",text="").grid(row=i+1,column=5)
        i7=Label(g,width=10,height=6,bg="white",text="").grid(row=i+1,column=6)'''


	#l.grid(row=0,column=1)
	#t1.pack()
        b1.place(x=300, y=500)
        b2.place(x=600 ,y=500)
        #b2.grid(row=i+1,column=2)
        #b1.place(anchor=S)
        root.withdraw()
        root1.withdraw
        g.mainloop()
        return g
