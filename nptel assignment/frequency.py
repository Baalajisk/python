def mlist(l):
    m=0
    mlist=[]
    for i in range(0,len(l)):
        if l.count(l[i])>m:
            m=l.count(l[i])
    for i in range(0,len(l)):
        if l.count(l[i])==m:
            if l[i] not in mlist:
                mlist.append(l[i])
    mlist.sort()
    return(mlist)
    
           
    
        
def milist(l):
    mi=l.count(l[0])
    milist=[]
    for i in range(1,len(l)):
        if l.count(l[i])<=mi:
            mi=l.count(l[i])
    for i in range(0,len(l)):
        if l.count(l[i])==mi:
            if l[i] not in milist:
                milist.append(l[i])
    milist.sort()
    return(milist)
    

def frequency(l):
    frequency=[]
    h=mlist(l)
    lo=milist(l)
    frequency.append(h)
    frequency.append(lo)
    return(tuple(frequency))
                
    
