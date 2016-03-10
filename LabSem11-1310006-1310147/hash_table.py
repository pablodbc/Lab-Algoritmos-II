from dlist import *
def f(x,tabla):
    A = 0.6180339887498949
    i = x
    Ai = A*i - int(A*i)
    return int(Ai*tabla.size)
class hashTable:

    def __init__(self, n):
        self.size = n
        self.slot = [ dlist() for i in xrange(n) ]
    def insertNode(self, node):
        m = f(node.key,self)
        j = self.slot[m].search(node.key)
        if j == None:
          self.slot[m].insert(node.key,node.data)
        else:
          j.data = node.data
    def insert(self,key,data):
        node = hashEntry(key,data)
        self.insertNode(node)
    def deleteNode(self,node):
        m = f(node.key,self)
        j = self.slot[m].search(node.key)
        if j != None:
            self.slot[m].delete(j)
    def delete(self,key):
        m = f(key,self)
        j = self.slot[m].search(key)
        if j != None:
            s = j.data
            self.slot[m].delete(j)
            return s
    def search(self,key):
        m = f(key,self)
        j = self.slot[m].search(key)
        if j != None:
            return j.data
    def __str__(self):
        print
        for i in xrange(len(self.slot)):
            print i+1,self.slot[i]
        return ""