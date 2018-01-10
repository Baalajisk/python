def transpose(l):
    t=[]
    rr=len(l)
    if type(l[0]) is list:
        cr=len(l[0])
    else:
        cr=1
    for i in range(0,cr):
        t.append([])
        for j in range(0,rr):
            t[i].append(l[j][i])
    return(t)
