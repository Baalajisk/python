def ascending(l):
    for i in range(0,len(l)-1):
        if l[i+1]<l[i]:
            return(False)
    return(True)
