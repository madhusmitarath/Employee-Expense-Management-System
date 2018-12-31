import sqlite3
con= sqlite3.connect('database.db')
p=con.cursor()
p.execute('''drop table if exists employee1''')

con.commit()

p.execute('''create table employee1 (name text not null, gender text, username text not null,designation text not null,password text,confirm_password text)''')

p.execute('''insert into employee1 (name, gender,username,designation,password,confirm_password) values (?,?,?,?,?,?);''',('name1','male','username1','Hardware engineer','xhvfs1','xhvfs1' ))
p.execute('''insert into employee1 (name, gender,username,designation,password,confirm_password) values (?,?,?,?,?,?);''',('name2','female','username2','Software engineer','xhvfs1','xhvfs1' ))
p.execute('''insert into employee1 (name, gender,username,designation,password,confirm_password) values (?,?,?,?,?,?);''',('name3','male','username3','Team leader','xhvfs1','xhvfs1' ))
p.execute('''insert into employee1 (name, gender,username,designation,password,confirm_password) values (?,?,?,?,?,?);''',('name4','female','username4','Associate engineer','xhvfs1','xhvfs1' ))
p.execute('''insert into employee1 (name, gender,username,designation,password,confirm_password) values (?,?,?,?,?,?);''',('name5','male','username5','Associate engineer','xhvfs1','xhvfs1' ))
p.execute('''insert into employee1 (name, gender,username,designation,password,confirm_password) values (?,?,?,?,?,?);''',('name6','male','username6','Software engineer','xhvfs1','xhvfs1' ))
con.commit()
'''result = p.execute(select * from employee1)
con.commit()'''
'''for row in result:
	print(row[0],end=', ')
	print(row[1],end=', ')
	print(row[2],end=', ')
	print(row[3],end=', ')
	print(row[4])'''


p.execute('''select username from employee1''')
result=p.fetchall()
#print(result)

p.execute('''drop table if exists applyvoucher''')
con.commit()
p.execute('''create table applyvoucher (username text not null, designation text, expense_date text,expense_purpose text,voucher text,payment text not null,status text)''')

p.execute('''insert into applyvoucher (username, designation,expense_date,expense_purpose,voucher,payment,status) values (?,?,?,?,?,?,?);''',('username1','Hardware engineer','2014-10-10','project','10000','cash','Pending'))
p.execute('''insert into applyvoucher (username, designation,expense_date,expense_purpose,voucher,payment,status) values (?,?,?,?,?,?,?);''',('username2','Software engineer','2016-10-11','project1','5000','cash','Approved'))
p.execute('''insert into applyvoucher (username, designation,expense_date,expense_purpose,voucher,payment,status) values (?,?,?,?,?,?,?);''',('username3','Team leader','2017-04-21','project2','5000','credit card','Rejected'))
p.execute('''insert into applyvoucher (username, designation,expense_date,expense_purpose,voucher,payment,status) values (?,?,?,?,?,?,?);''',('username4','Associate engineer','2017-06-28','project3','15000','cheque','Pending'))
p.execute('''insert into applyvoucher (username, designation,expense_date,expense_purpose,voucher,payment,status) values (?,?,?,?,?,?,?);''',('username5','Hardware engineer','2017-05-10','project4','10000','debit card','Approved'))
p.execute('''insert into applyvoucher (username, designation,expense_date,expense_purpose,voucher,payment,status) values (?,?,?,?,?,?,?);''',('username6','Software engineer','2017-10-12','project5','5000','cash','Rejected'))
con.commit()
#p.execute(" select * from applyvoucher where status='pending' order by expense_date")
#res=p.fetchall()
#print(res)

#result = p.execute('''select * from applyvoucher''')
#print(result)
#con.commit()
'''for row in result:

	print(row[1])
        print(row[2],end=', ')
	print(row[3],end=', ')
        print(row[4],end=', ')
        print(row[5])'''
