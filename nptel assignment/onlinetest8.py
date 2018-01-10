def maxcount(l):
    d={}
    for i in l:
        count=0
        for j in l:
            if i==j:
                count=count+1
        if i not in d.keys():
            d[i]=count
    v=[]
    for i in d.values():
        v.append(i)
    v.sort()
    return(v[-1])
