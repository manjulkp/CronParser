l="*/15 0 1,15 * 1-5 /usr/bin/find"
le=l.split(' ')

def toMin(mins):
	print "Minutes:",
	if "-" in mins:
		s=mins.split('-')
		for i in range(int(s[0]),int(s[1])+1):
			print i,
	elif(mins=="*"):
		for i in range(0,60):
			print i,
	elif "*/" in mins:
		d=mins.split('/')[1]
		for i in range(0,60,int(d)):
			print i,
	else:
		print mins,
	print
	
def toHrs(hrs):
	print "Hours:",
	if "-" in hrs:
		s=hrs.split('-')
		for i in range(int(s[0]),int(s[1])+1):
			print i,
	elif(hrs=="*"):
		for i in range(0,23):
			print i,
	elif "*/" in hrs:
		d=hrs.split('/')[1]
		for i in range(0,23,int(d)):
			print i,
	else:
		print hrs,
	print

def toDoM(dom):
	print "Day of month:",
	if "-" in dom:
		s=dom.split('-')
		for i in range(int(s[0]),int(s[1])+1):
			print i,
	elif(dom=="*"):
		for i in range(1,31):
			print i,
	elif "*/" in dom:
		d=dom.split('/')[1]
		for i in range(1,31,int(d)):
			print i,
	else:
		print dom,
	print

def toMon(mon):
	print "Month:",
	if "-" in mon:
		s=mon.split('-')
		for i in range(int(s[0]),int(s[1])+1):
			print i,
	elif(mon=="*"):
		for i in range(1,13):
			print i,
	elif "*/" in mon:
		d=mon.split('/')[1]
		for i in range(1,13,int(d)):
			print i,
	else:
		print mon,
	print
	
def toDoW(dow):
	print "Day of Week:",
	if "-" in dow:
		s=dow.split('-')
		for i in range(int(s[0]),int(s[1])+1):
			print i,
	elif(dow=="*"):
		for i in range(1,7):
			print i,
	elif "*/" in dow:
		d=dow.split('/')[1]
		for i in range(1,7,int(d)):
			print i,
	else:
		print dow,
	print
	
print '*'*3
toMin(le[0])
toHrs(le[1])
toDoM(le[2])
toMon(le[3])
toDoW(le[4])
print "Command: "+le[5]
print '*'*3