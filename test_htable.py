from hashEntry import *
from hash_table import *
from dlist import *
from random import*

tabla = hashTable(20)
for i in range(20):
	tabla.insert(randint(0,100),"holaJose")
print
print tabla
