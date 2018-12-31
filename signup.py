import sqlite3
from tkinter import messagebox
from tkinter import *
import employee
import manager
import valid
con = sqlite3.connect('database.db')
p=con.cursor()
                
def home(root,s):
        root.deiconify()
        s.destroy()
def back(v,c):
        v.deiconify()
        c.destroy()
			
def signup(root,root1,page):
        def store(value,c,page):
                flag=False
                if e1.get()=="" or e3.get()=="" or e4.get()=="" or e5.get()=="" or e6.get()=="":				#Condition to check Empty Fields
                        messagebox.showinfo("ERROR3","Each Field is Mandatory")
                else:
                        if valid.checkname(e1.get())==False:
                                messagebox.showinfo("ERROR5","Name cannot have any special character or number")
                        elif value!=1 and value!=2:
                                messagebox.showinfo("ERROR","Please,Select Your Gender!")
                        elif valid.checkusername(e3.get())==False:
                                messagebox.showinfo("Invalid Username","Username Must Be An Identifier")
                        elif valid.checkdesignation(e6.get())==False:
                                messagebox.showinfo("ERROR3","Designation cannot have any special characters or number")
                        elif valid.checkpassword(e4.get())==False:
                                messagebox.showinfo("\nPassword Should Be Minumum Of 6 Digit")
                        elif valid.checkconfirm_password(e4.get(),e5.get())==False:
                                messagebox.showinfo("ERRROR3","The Password Doesn't Match With The Above Password")
			
                        else:
                                
                                res=[]
                                result=p.execute('''select username from employee1''')
                                #con.commit()
                                '''for row in result:
                                        #print(row[0],end=', ')
                                        #print(row[1],end=', ')
                                        res.append(row[2])
                                        #print(row[3],end=', ')
                                        #print(row[4])'''
                                for row in result:																#Check if Similar Date and Time Exists
                                        if row[0]==e3.get():
                                                flag==True
                                                messagebox.showinfo("ERROR2","Username Already Exists")
                                                break
                                        if flag==False:
                                                if m.get()==1:
                                                        str_gender="Male"
                                                else:
                                                        str_gender="Female"
                                                #Add New Entry to Database
                                                p.execute("insert into '"+page+"' (name,gender,username,designation,password,confirm_password) values ( ?,?,?,?,?,? )",(e1.get(),str_gender,e3.get(),e6.get(),e4.get(),e5.get()))
                                                con.commit()

                                                messagebox.showinfo("Success","Succesfully Signed In")
                                                
                                                #result=con.execute('''select * from employee1''')
                                                #con.commit()
                                                '''for row in result:
                                                        print(row[0],end=', ')
                                                        print(row[1],end=', ')
                                                        print(row[2],end=', ')
                                                        print(row[3],end=', ')
                                                        print(row[4])'''
                                                root.deiconify()
                                                c.destroy()
                                                break
                                

					
        
        c=Toplevel(root)
        c.title("signup")
        c.minsize(1250,700)
        m = IntVar()
        background_img = PhotoImage(file="./bg2.png")
        background_label = Label(c,image=background_img)
        background_label.pack(fill=BOTH , expand=True)
	#BUTTON
        
        b10=Button(c, bg="firebrick4", fg="WHITE", text='BACK',font="Bold 10",pady=3.0,relief = FLAT,height=1,width=15,command=lambda : back(root,c))
        b10.place(x=600, y=600)

        b11=Button(c, bg="DEEP SKY BLUE",fg="black", text='SIGN IN',font="Bold 10",pady=3.0,relief = RAISED,height=1,width=15,command=lambda :store(m.get(),c,page))
        b11.place(x=50, y=550)

        l1=Label(c,font="Bold 15",fg="black",bg="mistyrose3",text="Name  : ")
        l2=Label(c,font="Bold 15",fg="black",bg="mistyrose3",text="Gender  : ")
        l3=Label(c,font="Bold 15",fg="black",bg="mistyrose3",text="Username  : ")
        l6=Label(c,font="Bold 15",fg="black",bg="mistyrose3",text="Designation :")
        l4=Label(c,font="Bold 15",fg="black",bg="mistyrose3",text="Password  : ")
        l5=Label(c,font="Bold 15",fg="black",bg="mistyrose3",text="Confirm Password : ")
        
        b2=Radiobutton(c, text="male",bg="mistyrose3",font=(None, 12), variable=m , value=1)
        b3=Radiobutton(c, text="female", bg="mistyrose3",font=(None, 12),variable=m ,value=2)
        b2.place(x=200, y=280)
        b3.place(x=300, y=280)
        
        
        l1.place(x=50, y=230)
        l2.place(x=50, y=280)
        l3.place(x=50, y=330)
        l4.place(x=50, y=410)
        l5.place(x=50, y=460)
        l6.place(x=50, y=380)
        
        e1=Entry(c)
        e3=Entry(c)
        e4=Entry(c,show="*")
        e5=Entry(c,show="*")
        e6=Entry(c)
        
        e1.place(x=200, y=230)
        e3.place(x=200, y=330)
        e4.place(x=200, y=410)
        e5.place(x=250, y=460)
        e6.place(x=200, y=380)
        

        
        
        root.withdraw()
        root1.withdraw()
        c.mainloop()
        return c

        
