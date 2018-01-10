def maxbad(l):
  end = len(l) - 1
  mymax = l[-1]
  for i in range(end,0,-1):
    if l[i] > mymax:
       mymax = l[i]
  return(mymax)
