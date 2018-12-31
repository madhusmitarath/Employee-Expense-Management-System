from tkinter import *
import account_details
	
def home(root,s):
	root.deiconify()
	s.destroy()
def back(v,c):
        v.deiconify()
        c.destroy()
			
def login_admin(root,root1):
        i=3
        x=Toplevel(root)
        x.title("login")
        x.minsize(1250,700)
        background_img = PhotoImage(file="./bg3.png")
        background_label = Label(x,image=background_img)
        background_label.pack(fill=BOTH , expand=True)
	
	
	#BUTTON
        

        b10=Button(x, bg="deep sky blue", fg="black", text='Sign Out',font="Bold 10",pady=3.0,relief = RAISED,height=1,width=15,command=lambda : back(root,x))
        b10.place(x=600, y=600)
        
        b3=Button(x, bg="black",fg="white", text='ACCOUNT DETAILS',font="Bold 15",pady=3.0,relief = FLAT,height=1,width=20,command=lambda : account_details.account_details(x,root))
        b3.place(x=102, y=150)
        #b4=Button(x, bg="black", fg="white", text='REMOVE EMPLOYEE',font="Bold 15",pady=3.0,relief = FLAT,height=1,width=20,command=lambda : delete_employee.delete_employee(x,root))
        #b4.place(x=102, y=200)
        #b5=Button(x, bg="black", fg="white", text='REMOVE MANAGER',font="Bold 15",pady=3.0,relief = FLAT,height=1,width=20,command=lambda : delete_manager.delete_manager(x,root))
        #b5.place(x=102, y=250)
        

        root.withdraw()
        root1.withdraw()
        x.mainloop()

        return x

        
