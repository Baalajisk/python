roll={}
n=input("enter the range of students:")
for i in range(n):
    rollno=input("enter the roll number:")
    name=raw_input("enter the name:")
    roll[rollno]=name
std=input("enter the roll number to search:")
try:
    print roll[std]
except:
    print "no such roll number"
