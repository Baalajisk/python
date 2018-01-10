def sublist(l1,l2):
    le=len(l1)
    flag=0
    for i in range(0,len(l2)):
        if l1==l2[i:le]:
            flag=flag+1
        le=le+1
    if flag>0:
        return(True)
    else:
        return(False)
        
