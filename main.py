from tkinter import *
import tkinter
import os
import employee
import manager
import admin
#import database

root = Tk()
root.minsize(1250,700)

root.title("EMPLOYEE EXPENSE MANAGEMENT SYSTEM")
background_img = PhotoImage(file="./bg.png")
background_label = Label(root,image=background_img)
background_label.pack(fill=BOTH , expand=True)

#BUTTON5
b1=Button(root, bg="firebrick4",fg="white", text='HOME',font="Bold 10",pady=3.0,relief = FLAT,height=1,width=15)
b1.place(x=600, y=20)

b2=Button(root, bg="firebrick4", fg="white", text='MANAGER',font="Bold 10",pady=3.0,relief = FLAT,height=1,width=15,command=lambda : manager.manager(root))
b2.place(x=750, y=20)

b3=Button(root, bg="firebrick4", fg="white", text='EMPLOYEE',font="Bold 10",pady=3.0,relief = FLAT,height=1,width=15,command=lambda : employee.employee(root))
b3.place(x=900, y=20)

b4=Button(root, bg="firebrick4",fg="white", text='ADMIN',font="Bold 10",pady=3.0,relief = FLAT,height=1,width=15,command=lambda : admin.admin(root))
b4.place(x=1050, y=20)

root.mainloop()
