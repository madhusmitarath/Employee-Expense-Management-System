def checkname(name):
    if all(x.isalpha() or x.isspace() for x in name):
        return True
    else:
        return False


def checkdesignation(designation):
    if all(x.isalpha() or x.isspace() for x in designation):
        return True
    else:
        return False

def checkusername(username):
    if username.isidentifier():
        return True
    else:
        return False
    

def checkpassword(password):
        if len(password)<6 :
            return False
        else:
            return True


def checkconfirm_password(password,confirm_password):
    if password==confirm_password:
        return True
    else:
        return False
    
def checkdate(date):
	c=0
	for i in date:
		if i=='-':
			c+=1
	if c!=2:
		return False
		
	day,month,year=date.split('-')
	if len(day)!=2 or len(month)!=2 or len(year)!=4:
		return False
	try:
		year=int(year)
		month=int(month)
		day=int(day)
	except(ValueError):
		return False
		
	if month>12 or month<1:
			return False	
	if month in [1,3,5,7,8,10,12]:
		if day>31 or day<1:
			return False
	if month in [4,6,9,11]:
		if day>30 or day<1:
			return False
				
	if(year%400==0 or (year%4==0 and year%100!=0)):
		if month==2 and (day>29 or day<1):
			return False
	else:		
		if month==2 and (day>28 or day<1):
			return False
	
	return True
    
