class student:
    count=0
    def __init__(self,name,idno):
        self.name=name
        self.idno=idno
        self.count=1
    def display(self):
        print "",self.name,"'s id is ",self.idno
    def display_count(self):
        print"the count is ",self.count
class school(student):
    def __init__(self):
        print "this is a inherited class"

s1=student("baalaji",2)
s2=student("sk",1)
s1.display()
s1.display_count()
s2.display()
s2.display_count()
sc=school()
