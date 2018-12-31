import sqlite3
con= sqlite3.connect('database.db')
p=con.cursor()
p.execute('''drop table if exists manager''')
con.commit()

p.execute('''create table manager (name text not null, gender text, username text not null,designation text not null,password text,confirm_password text)''')

p.execute('''insert into manager (name, gender,username,designation,password,confirm_password) values (?,?,?,?,?,?);''',('name1','male','username1','Team leader','xhvfs1','xhvfs1' ))
p.execute('''insert into manager (name, gender,username,designation,password,confirm_password) values (?,?,?,?,?,?);''',('name2','female','username2','Team leader','xhvfs1','xhvfs1' ))
p.execute('''insert into manager (name, gender,username,designation,password,confirm_password) values (?,?,?,?,?,?);''',('name3','male','username3','Team leader','xhvfs1','xhvfs1' ))
p.execute('''insert into manager (name, gender,username,designation,password,confirm_password) values (?,?,?,?,?,?);''',('name4','female','username4','Team leader','xhvfs1','xhvfs1' ))
p.execute('''insert into manager (name, gender,username,designation,password,confirm_password) values (?,?,?,?,?,?);''',('name5','male','username5','Team leader','xhvfs1','xhvfs1' ))
p.execute('''insert into manager (name, gender,username,designation,password,confirm_password) values (?,?,?,?,?,?);''',('name6','male','username6','Team leader','xhvfs1','xhvfs1' ))
con.commit()
result = p.execute('''select * from manager''')
con.commit()
'''for row in result:
	print(row[0],end=', ')
	print(row[1],end=', ')
	print(row[2],end=', ')
	print(row[3],end=', ')
	print(row[4])'''



