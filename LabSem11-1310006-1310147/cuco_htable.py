def f1(x,tabla):
	A = 0.6180339887498949
	i = x
	Ai = A*i - int(A*i)
	return int(Ai*tabla.size)
def f2(x,tabla):
	return x%tabla.size
#######################################################################################
class cucoEntry:
	def __init__(self,key,data):
		self.key = key
		self.data = data
########################################################################################
class cucoTable:
	def __init__(self,size):
		self.size = size
		self.slot = [None for i in xrange(size)]
	def insert(self,key,data):
		pos = f1(key,self)
		node = cucoEntry(key,data)
		for i in xrange(self.size+1):
			if self.slot[pos] == None:
				self.slot[pos] = node
				return 1
			elif self.slot[pos] != None and node.key == self.slot[pos].key:
				self.slot[pos].data = node.data
				return 1
			else:
				node,self.slot[pos] = self.slot[pos],node
				if pos == f1(node.key,self):
					pos = f2(node.key,self)
				else:
					pos = f1(node.key,self)
	def search(self,key):
		i = f1(key,self)
		j = f2(key,self)
		if self.slot[i] != None and self.slot[i].key == key:
			return self.slot[i].data
		if self.slot[j] != None and self.slot[j].key == key:
			return self.slot[j].data
	def delete(self,key):
		i = f1(key,self)
		j = f2(key,self)
		if self.slot[i] != None and self.slot[i].key == key:
			a = self.slot[i].data
			self.slot[i] = None
			return a
		if self.slot[j] != None and self.slot[j].key == key:
			a = self.slot[j].data
			self.slot[j] = None
			return a
	def __str__(self):
		for i in xrange(self.size):
			if self.slot[i] != None:
				print i+1, self.slot[i].key, self.slot[i].data
			else:
				print i+1, None
		return ""



		