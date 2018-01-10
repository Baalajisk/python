def mlist(l):
    m=0
    mlist=[]
    for i in range(0,len(l)):
        if l[i]>m:
            m=l[i]
    for i in range(0,len(l)):
        if l.count(l[i])==m:
            if l[i] not in mlist:
                mlist.append(l[i])
    return(mlist)
    
           
    
        
def milist(l):
    mi=l[0]
    milist=[]
    for i in range(1,len(l)):
        if l[i]<=mi:
            mi=l[i]
    for i in range(0,len(l)):
        if l.count(l[i])==mi:
            if l[i] not in milist:
                milist.append(l[i])
    return(milist)
    

def frequency(l):
    frequency=[]
    high=mlist(l)
    low=milist(l)
    frequency.append(high)
    frequency.append(low)
    return(frequency)
                
    
