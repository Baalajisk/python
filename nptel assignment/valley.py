
 
          
def valley(l):
    dec=0
    inc=1
    i=0
    while len(l)>=3 and l[i]>l[i+1]:
        if i<len(l)-1:
            (dec,i)=(dec+1,i+1)
    while i<len(l)-1:
        if l[i]<l[i+1]:
            
            (inc,i)=(inc+1,i+1)
        else:
            return(False)
    if i==len(l)-1:
        if dec>=2 and inc>=2:
            return(True)
        else:
          return(False)
    
        
