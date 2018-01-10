               
def tolist(l):
    li=[]
    for i in range(0,len(l)):
        li.append(list(l[i]))
    return(li)

def totuple(li):
    for i in range(0,len(li)):
        li[i]=tuple(li[i])
    return(li)

def onehop(l):
    li=tolist(l)
    one=[]
    for i in range(0,len(li)):
        for j in range(i,len(li)):
            if li[i][1]==li[j][0] and li[i][0]!=li[j][1]:
                if li[i][0] not in one and li[j][1] not in one:
                    one.append([li[i][0],li[j][1]])
        
            elif li[i][0]==li[j][1] and li[i][1]!=li[j][0]:
                if li[j][0] not in one and li[i][1] not in one:
                    one.append([li[j][0],li[i][1]])
                           
    onehop=totuple(one)
    onehop.sort()
    for i in onehop:
        while onehop.count(i)>1:
            
            onehop.remove(i)
    return(onehop)
l=input("enter the list")
o=onehop(l)    
print(o)
        
                   
    
        
            
        
        
        
        
            
            

