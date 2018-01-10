import random
def getmax(a,b):
	if a>b:
		return a
	else:
		return b
num1=random.randint(1,500)
num2=random.randint(1,500)
for i in range(50):
	print "max of %d and %d is %d"%(num1,num2,getmax(num1,num2)
