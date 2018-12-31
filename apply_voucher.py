import sqlite3
from tkinter import messagebox
from tkinter import *
import employee
import valid
import login
	
def home(root,s):
	root.deiconify()
	s.destroy()
def back(v,c):
        v.deiconify()
        c.destroy()
			
def apply_voucher(root,root1,name,desig):
        con = sqlite3.connect('database.db')
        p = con.cursor()
        def voucher(name,desig):
                flag=False
                if e1.get()=="" or e3.get()=="" or e4.get()=="":				#Condition to check Empty Fields
                        messagebox.showinfo("ERROR3","Each Field is Mandatory")
                else:
                        if name!=e1.get():
                                messagebox.showinfo("ERROR","Username Do Not Match")
                        elif desig!=tkvar.get():
                                messagebox.showinfo("ERROR","Designation Do Not Match")
                        elif valid.checkdate(e3.get())==False:
                                messagebox.showinfo("ERROR","Date Format Error\nDate Format :dd-mm-yyyy")
                        else:
                                flag=False
                                p.execute("select expense_date from applyvoucher where username='"+e1.get()+"';")
                                res=p.fetchall()
                                for row in res:
                                        if row[0]==e3.get():
                                                flag=True
                                if flag==True:
                                        messagebox.showinfo("ERROR","Cannot apply more than one voucher on the same day")
                                elif flag == False:          
                                        result=p.execute('''select * from applyvoucher''')
                                        if m.get()==1:
                                                int_voucher=5000
                                        elif m.get()==2:
                                                int_voucher=10000
                                        else:
                                                int_voucher=15000
                                                #Add New Entry to Database
                                        p.execute('''insert into applyvoucher (username,designation,expense_date,expense_purpose,voucher,payment,status) values ( ?,?,?,?,?,?,? )''',(e1.get(),tkvar.get(),e3.get(),e4.get(),int_voucher,tkvar1.get(),"Pending"))
                                        con.commit()
                                        messagebox.showinfo("Success","Voucher Applied")
                                        e1.delete(0,'end')
                                        #e2.delete(0,'end')
                                        e3.delete(0,'end')
                                        e4.delete(0,'end')

                                        
	
	#BUTTON
        i=3
        d=Toplevel(root)
        d.title("apply voucher")
        d.minsize(1250,700)
        m = IntVar()
        tkvar=StringVar()
        tkvar1=StringVar()
        background_img = PhotoImage(file="./bg2.png")
        background_label = Label(d,image=background_img)
        background_label.pack(fill=BOTH , expand=True)
        
        b10=Button(d, bg="firebrick4", fg="WHITE", text='BACK',font="Bold 10",pady=3.0,relief = FLAT,height=1,width=15,command=lambda : back(root,d))
        b10.place(x=300, y=600)

        res=[]
        result=p.execute("select distinct designation from employee1")
        #result=p.fetchall()
        for row in result:
                res.append(row[0])
               
        #print(res)
        tkvar.set(res[0])
        popupMenu=OptionMenu(d,tkvar, *res)
        popupMenu.place(x=200,y=260)
        
        
        choices1={'Cash','Cheque','Debit Crad','Credit Card'}
        tkvar1.set('Cash')

        popupMenu=OptionMenu(d,tkvar1, *choices1)
        popupMenu.place(x=200, y=460)
        
        l1=Label(d,font="Bold 15",fg="BLACK",bg="mistyrose3",text="Username : ")
        l2=Label(d,font="Bold 15",fg="BLACK",bg="mistyrose3",text="Designation : ")
        l3=Label(d,font="Bold 15",fg="BLACK",bg="mistyrose3",text="Expense Date  : ")
        l4=Label(d,font="Bold 15",fg="BLACK",bg="mistyrose3",text="Expense Purpose: ")
        l5=Label(d,font="Bold 15",fg="BLACK",bg="mistyrose3",text="Voucher : ")
        l6=Label(d,font="Bold 15",fg="BLACK",bg="mistyrose3",text="Payment : ")
        
        b3=Radiobutton(d, text="5000",bg="mistyrose3",font=(None, 12), variable=m , value=1)
        b4=Radiobutton(d, text="10,000", bg="mistyrose3",font=(None, 12),variable=m ,value=2)
        b7=Radiobutton(d, text="15,000",bg="mistyrose3",font=(None, 12), variable=m , value=3)
        b3.place(x=200, y=410)
        b4.place(x=300, y=410)
        b7.place(x=400, y=410)
        
        l1.place(x=50, y=210)
        l2.place(x=50, y=260)
        l3.place(x=50, y=310)
        l4.place(x=50, y=360)
        l5.place(x=50, y=410)
        l6.place(x=50, y=460)

        
        e1=Entry(d)
        #e2=Entry(d)
        e3=Entry(d)
        e4=Entry(d,width=30)
        
        
        
        e1.place(x=200, y=210)
        #e2.place(x=200, y=260)
        e3.place(x=230, y=310)
        e4.place(x=230, y=365) 
       # e6.place(x=200, y=460)

        b11=Button(d, bg="DEEP SKY BLUE",fg="Black", text='SEND',font="Bold 10",pady=3.0,relief = RAISED,height=1,width=15,command=lambda :voucher(name,desig))
        b11.place(x=50, y=550)       
        
        
        root.withdraw()
        root1.withdraw()
        d.mainloop()

        return d

        

