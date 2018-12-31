import sqlite3
from tkinter import *
import manager
import employee
import employee_request
import total_approved
	
def home(root,s):
	root.deiconify()
	s.destroy()
def back(v,c):
        v.deiconify()
        c.destroy()
			
def login_manager(root,root1):
        i=3
        f=Toplevel(root)
        f.title("login manager")
        f.minsize(1250,700)
        background_img = PhotoImage(file="./bg3.png")
        background_label = Label(f,image=background_img)
        background_label.pack(fill=BOTH , expand=True)
	
        con=sqlite3.connect('database.db')
        p=con.cursor()
        p.execute("select status from applyvoucher where status='Pending'")
        res=p.fetchall()
        c=0
        for row in res:
                c+=1
	#BUTTON
        

        b10=Button(f, bg="DEEP SKY BLUE", fg="black", text='SIGN OUT',font="Bold 10",pady=3.0,relief = RAISED,height=1,width=15,command=lambda : back(root,f))
        b10.place(x=600, y=600)
        
        b3=Button(f, bg="black",fg="white", text='EMPLOYEE REQUEST: %s'%(c),font="Bold 15",pady=3.0,relief = FLAT,height=1,width=20,command=lambda :employee_request.employee_request(f,root))
        b3.place(x=90, y=150)
        b4=Button(f, bg="black", fg="white", text='TOTAL APPROVAL',font="Bold 15",pady=3.0,relief = FLAT,height=1,width=20,command=lambda :total_approved.total_approved(f,root))
        b4.place(x=90, y=200)
        

        
        root.withdraw()
        root1.withdraw()
        f.mainloop()

        return f
