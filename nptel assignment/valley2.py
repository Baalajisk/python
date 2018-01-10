def valley(l):
    flag1=0
    flag2=0
    dec=1
    inc=1
    i=0
    while l[i]>l[i+1] and i<len(l)-1:
        dec=dec+1
        if dec>=2:
            flag1=1
        i=i+1
    while i<len(l)-1:
        if l[i]<l[i+1]:
            inc=inc+1
            if inc>=2:
                flag2=1
        else:
            return(False)
        i=i+1
    if flag1==1 and flag2==1:
        return(True)
    else:
        return(False)
        
        
        
        
