"""sorting names"""
n=input("enter the limit:")
count=0
names=[]
print "enter the names"
while(n>count):
	names.insert(count,input())
	count=count+1
names.sort()
for name in names:
	print name

	
