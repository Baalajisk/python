class add(object):
	def __init__(self,a,b):
		self.a=a
		self.b=b
	c=a+b	
	def __str__(self):
		return "the sum is %s"%(c)

		
sum=add(3,5)
print sum
	
