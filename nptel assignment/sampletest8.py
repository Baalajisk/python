def repeated(l):
    c=[]
    
    for i in l:
        if l.count(i)>1 and i not in c:
            c.append(i)
            
    return(len(c))
