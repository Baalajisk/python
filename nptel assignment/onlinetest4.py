def myreverse(l):
    if l==[]:
        return(l)
    else:
        return(
            [l[-1]]+myreverse(l[:-1]))
