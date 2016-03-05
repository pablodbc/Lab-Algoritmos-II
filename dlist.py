from hashEntry import *
class dlist:

	def __init__(self):
		self.head = None

	def insert(self, key, data):
		node = hashEntry(key, data)
		node.next = self.head
		if self.head != None:
			self.head.prev = node
		self.head = node

	def search(self, key):
		node = self.head
		while node != None and node.key != key:
			node = node.next
		return node

	def delete(self, node):
		if node.prev != None:
			node.prev.next = node.next
		else:
			self.head = node.next
		if node.next != None:
			node.next.prev = node.prev
		
	def __str__(self):
		i = self.head
		a = []
		while i != None:
			a.append((i.key,i.data))
			i = i.next
		a.append(None)
		print a
		return ""
