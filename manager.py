import sqlite3
from tkinter import *
from tkinter import messagebox
import signup
import employee
import admin
import login_manager
#import manager_table

def home(root,s):
	root.deiconify()
	s.destroy()	

def manager(root):
        def store(a):
                if e1.get()=="" or e2.get()=="":				#Condition to check Empty Fields
                        messagebox.showinfo("ERROR3","Each Field is Mandatory")
                        print("error1")
			
                else:
                        con = sqlite3.connect('database.db')
                        p = con.cursor()
                        res=[]
                        result=p.execute('''select username from manager''')
                        #con.commit()
                        '''for row in result:
                                        #print(row[0],end=', ')
                                        #print(row[1],end=', ')
                                res.append(row[2])
                                        #print(row[3],end=', ')
                                        #print(row[4])'''
                                
                        for row in result:
                                if row[0]==e1.get():
                                        result1=p.execute("select * from manager where username='"+e1.get()+"';")
                                        #con.commit()
                                        print(result1)
                                        for row in result1:
                                                pas=row[4]
                                                #print(pas)
                                        if pas==e2.get():
                                                messagebox.showinfo("Success","Logged In Successfully")
                                                e1.delete(0,'end')
                                                e2.delete(0,'end')
                                                login_manager.login_manager(a,root)
                                                break
                        else:
                                flag=False
                                p.execute("select username from manager")
                                res=p.fetchall()
                                for row in res:
                                        if row[0]==e1.get():
                                                flag=True
                                #print(flag)
                                if flag==False:
                                        messagebox.showinfo("Error","Wrong Username")
                                else:
                                        flag=False
                                        p.execute("select password from manager where username='"+e1.get()+"';")
                                        res1=p.fetchall()
                                        for row in res1:
                                                if row[0]==e2.get():
                                                        flag=True
                                        #print(flag)
                                        if flag==False:
                                                messagebox.showinfo("Error","Wrong password")
                                a.deiconify()
        i=3
        a=Toplevel(root)
        a.title("manager")
        a.minsize(1250,700)
        background_img = PhotoImage(file="./bg1.png")
        background_label = Label(a,image=background_img)
        background_label.pack(fill=BOTH , expand=True)
	
	#BUTTON

        b1=Button(a, bg="steelblue2",fg="black", text='HOME',font="Bold 10",pady=3.0,relief = FLAT,height=1,width=15,command=lambda : home(root,a))
        b1.place(x=600, y=20)
        b2=Button(a, bg="white", fg="black", text='MANAGER',font="Bold 10",pady=3.0,relief = GROOVE,height=1,width=15)
        b2.place(x=750, y=20)

        b3=Button(a, bg="steelblue2", fg="black", text='EMPLOYEE',font="Bold 10",pady=3.0,relief = FLAT,height=1,width=15,command=lambda : employee.employee(a))
        b3.place(x=900, y=20)

        b4=Button(a, bg="steelblue2",fg="black", text='ADMIN',font="Bold 10",pady=3.0,relief = FLAT,height=1,width=15,command=lambda : admin.admin(a))
        b4.place(x=1050, y=20)

        l1=Label(a,font="Bold 15",fg="BLACK",bg="lightcyan",text="Username : ")
        l2=Label(a,font="Bold 15",fg="BLACK",bg="lightcyan",text="Password  : ")
        e1=Entry(a)
        e2=Entry(a,show="*")
        l1.place(x=500, y=250) 
        l2.place(x=500, y=300)
        e1.place(x=700, y=250)
        e2.place(x=700, y=300)
        b5=Button(a, bg="DEEP SKY BLUE",fg="black", text='LOGIN',font="Bold 10",pady=3.0,relief = RAISED,height=1,width=15,command=lambda : store(a))
        b5.place(x=600, y=350)
        b5=Button(a, bg="lightcyan",fg="NAVY BLUE", text='New User? Sign Up Here.',font="Bold 15",pady=3.0,relief = FLAT,height=1,width=20,command=lambda : signup.signup(a,root,"manager"))
        b5.place(x=580, y=390)
        root.withdraw()
        a.mainloop()

        return a
