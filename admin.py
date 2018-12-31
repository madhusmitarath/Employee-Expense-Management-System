from tkinter import *
from tkinter import messagebox
import manager
import employee
import login_admin
def home(root,s):
	root.deiconify()
	s.destroy()

def admin(root):

        def store(e1,e2):
                if e1=="" or e2=="":				#Condition to check Empty Fields
                        messagebox.showinfo("ERROR3","Each Field is Mandatory")
			
                elif e1=='admin' and e2=='123456':
                        messagebox.showinfo("Success","Logged In Successfully")
                        #e1.delete(0,'end')
                        #e2.delete(0,'end')
                        login_admin.login_admin(o,root)
                                #break
                else:
                        if e1!="admin":
                                messagebox.showinfo("Wrong Username")
                        else:
                                messagebox.showinfo("Wrong Password")
                       
                        
        i=3
        o=Toplevel(root)
        o.title("account_details")
        o.minsize(1250,700)
        background_img = PhotoImage(file="./bg1.png")
        background_label = Label(o,image=background_img)
        background_label.pack(fill=BOTH , expand=True)

        #print(employee)
	
	#BUTTON

        b1=Button(o, bg="steelblue2",fg="black", text='HOME',font="Bold 10",pady=3.0,relief = FLAT,height=1,width=15,command=lambda : home(root,o))
        b1.place(x=600, y=20)
        b2=Button(o, bg="steelblue2", fg="black", text='MANAGER',font="Bold 10",pady=3.0,relief = FLAT,height=1,width=15,command=lambda : manager.manager(o))
        b2.place(x=750, y=20)

        b3=Button(o, bg="steelblue2", fg="black", text='EMPLOYEE',font="Bold 10",pady=3.0,relief = FLAT,height=1,width=15,command=lambda : employee.employee(o))
        b3.place(x=900, y=20)

        b4=Button(o, bg="white",fg="black", text='ADMIN',font="Bold 10",pady=3.0,relief = FLAT,height=1,width=15)
        b4.place(x=1050, y=20)

        l1=Label(o,font="Bold 15",fg="BLACK",bg="lightcyan",text="Username: ")
        l2=Label(o,font="Bold 15",fg="BLACK",bg="lightcyan",text="Password  : ")
        e1=Entry(o)
        e2=Entry(o,show="*")
        l1.place(x=500, y=250) 
        l2.place(x=500, y=300)
        e1.place(x=700, y=250)
        e2.place(x=700, y=300)
        
        b5=Button(o, bg="DEEP SKY BLUE",fg="Black", text='LOGIN',font="Bold 10",pady=3.0,relief = RAISED,height=1,width=15,command=lambda : store(e1.get(),e2.get()))
        b5.place(x=600, y=350)
        

        root.withdraw()
        o.mainloop()

        return o

              



        
