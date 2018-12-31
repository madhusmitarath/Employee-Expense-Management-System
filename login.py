from tkinter import *
import employee
import apply_voucher
import checkstatus
import delete_voucher
	
def home(root,s):
	root.deiconify()
	s.destroy()
def back(v,c):
        v.deiconify()
        c.destroy()
			
def login(root,root1,name,desig):
        i=3
        m=Toplevel(root)
        m.title("login")
        m.minsize(1250,700)
        background_img = PhotoImage(file="./bg3.png")
        background_label = Label(m,image=background_img)
        background_label.pack(fill=BOTH , expand=True)
	
	
	#BUTTON

        #b1=Button(m, bg="MAROON",fg="WHITE", text='HOME',font="Bold 10",pady=3.0,relief = FLAT,height=1,width=15,command=lambda : home(root1,m))
        #b1.place(x=900, y=20)
     
        #b2=Button(m, bg="MAROON", fg="WHITE", text='MANAGER',font="Bold 10",pady=3.0,relief = FLAT,height=1,width=15,command=lambda : manager.manager(m))
        #b2.place(x=750, y=20)

        #b5=Button(m, bg="MAROON", fg="WHITE", text='EMPLOYEE',font="Bold 10",pady=3.0,relief = FLAT,height=1,width=15,command=lambda : employee.employee(m))
        #b5.place(x=900, y=20)

        #b6=Button(m, bg="MAROON",fg="WHITE", text='ACCOUNT DETAILS',font="Bold 10",pady=3.0,relief = FLAT,height=1,width=15,command=lambda : account_details.account_details(m))
        #b6.place(x=1050, y=20)
        

        b10=Button(m, bg="DEEP SKY BLUE", fg="Black", text='SIGN OUT',font="Bold 10",pady=3.0,relief = RAISED,height=1,width=15,command=lambda : back(root,m))
        b10.place(x=600, y=600)
        
        b3=Button(m, bg="black",fg="white", text='APPLY FOR VOUCHER',font="Bold 15",pady=3.0,relief = FLAT,height=1,width=20,command=lambda : apply_voucher.apply_voucher(m,root,name,desig))
        b3.place(x=102, y=150)
        b4=Button(m, bg="black", fg="white", text='CHECK FOR STATUS',font="Bold 15",pady=3.0,relief = FLAT,height=1,width=20,command=lambda : checkstatus.checkstatus(m,root,name))
        b4.place(x=102, y=200)
        b5=Button(m, bg="black", fg="white", text='DELETE VOUCHER',font="Bold 15",pady=3.0,relief = FLAT,height=1,width=20,command=lambda : delete_voucher.delete_voucher(m,root,name))
        b5.place(x=102, y=250)
        

        root.withdraw()
        root1.withdraw()
        m.mainloop()

        return m

        
