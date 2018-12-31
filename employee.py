import sqlite3
from tkinter import *
from tkinter import messagebox
import signup
import manager
import admin
import login

con = sqlite3.connect('database.db')
p = con.cursor()
def home(root,s):
	root.deiconify()
	s.destroy()

def employee(root):

        def store(v):
                if e1.get()=="" or e2.get()=="":				#Condition to check Empty Fields
                        messagebox.showinfo("ERROR3","Each Field is Mandatory")
			
                else:
                       
                        res=[]
                        p.execute('''select username from employee1''')
                        result=p.fetchall()
                        for row in result:
                                if row[0]==e1.get():
                                        p.execute("select password from employee1 where username='"+e1.get()+"';")
                                        result1=p.fetchall()
                                        name=e1.get()
                                        if result1[0][0]==e2.get():
                                                messagebox.showinfo("Success","Logged In Successfully")
                                                p.execute("select designation from employee1 where username='"+e1.get()+"';")
                                                result2=p.fetchall()
                                                desig=result2[0][0]
                                                e1.delete(0,'end')
                                                e2.delete(0,'end')
                                                login.login(v,root,name,desig)
                                                break
                        else:
                                flag=False
                                p.execute("select username from employee1")
                                res=p.fetchall()
                                for row in res:
                                        if row[0]==e1.get():
                                                flag=True
                                #print(flag)
                                if flag==False:
                                        messagebox.showinfo("Error","Wrong Username")
                                else:
                                        flag=False
                                        p.execute("select password from employee1 where username='"+e1.get()+"';")
                                        res1=p.fetchall()
                                        for row in res1:
                                                if row[0]==e2.get():
                                                        flag=True
                                        #print(flag)
                                        if flag==False:
                                                messagebox.showinfo("Error","Wrong password")
                                v.deiconify()
        i=3
        v=Toplevel(root)
        v.title("employee")
        v.minsize(1250,700)
        background_img = PhotoImage(file="./bg1.png")
        background_label = Label(v,image=background_img)
        background_label.pack(fill=BOTH , expand=True)
        #employee="employee"

        #print(employee)
	
	#BUTTON

        b1=Button(v, bg="steelblue2",fg="black", text='HOME',font="Bold 10",pady=3.0,relief = FLAT,height=1,width=15,command=lambda : home(root,v))
        b1.place(x=600, y=20)
        b2=Button(v, bg="steelblue2", fg="black", text='MANAGER',font="Bold 10",pady=3.0,relief = FLAT,height=1,width=15,command=lambda : manager.manager(v))
        b2.place(x=750, y=20)

        b3=Button(v, bg="white", fg="black", text='EMPLOYEE',font="Bold 10",pady=3.0,relief = GROOVE,height=1,width=15)
        b3.place(x=900, y=20)

        b4=Button(v, bg="steelblue2",fg="black", text='ACCOUNT DETAILS',font="Bold 10",pady=3.0,relief = FLAT,height=1,width=15,command=lambda : admin.admin(v))
        b4.place(x=1050, y=20)

        l1=Label(v,font="Bold 15",fg="BLACK",bg="lightcyan",text="Username: ")
        l2=Label(v,font="Bold 15",fg="BLACK",bg="lightcyan",text="Password  : ")
        e1=Entry(v)
        e2=Entry(v,show="*")
        l1.place(x=500, y=250) 
        l2.place(x=500, y=300)
        e1.place(x=700, y=250)
        e2.place(x=700, y=300)
        
        b5=Button(v, bg="DEEP SKY BLUE",fg="Black", text='LOGIN',font="Bold 10",pady=3.0,relief = RAISED,height=1,width=15,command=lambda : store(v))
        b5.place(x=600, y=350)
        b6=Button(v, bg="lightcyan",fg="NAVY BLUE", text='New User? Sign Up Here.',font="Bold 15",pady=3.0,relief = FLAT,height=1,width=20,command=lambda : signup.signup(v,root,"employee1"))
        b6.place(x=580, y=390)

        
        #c=con.cursor()
        #result=c.execute('''select * from employee1''')
        '''con.commit()
        for row in result:
                        print(row[0],end=', ')
                        print(row[1],end=', ')
                        print(row[2],end=', ')
                        print(row[3],end=', ')
                        print(row[4])'''

        root.withdraw()
        v.mainloop()

        return v

              



        
