def f1(x,tabla):
	A = 0.6180339887498949
	i = x
	Ai = A*i - int(A*i)
	return int(Ai*tabla.size)
def f2(x,tabla):
	A = 1 - 0.6180339887498949
	i = x
	Ai = A*i - int(A*i)
	return int(Ai*tabla.size)
class cucoEntry:
	def __init__(self,key,data):
		self.key = key
		self.data = data
class cucoTable:
	def __init__(self,size):
		self.size = size
		self.slot = [None for i in range(size)]
	def insert(self,key,data):
		pos = f1(key,self)
		