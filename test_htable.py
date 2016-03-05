from hashEntry import *
from hash_table import *
from dlist import *
from random import *
from string import *

def checkSize(valorEsperado, valorReal):
	if valorReal == valorEsperado:
		return True
	else:
		return False
def randomstr(N):
	return ''.join(choice(lowercase) for i in range(N))
def checkNodeInsertion(tabla):
	key = randint(0,tabla.size-1)
	data = randomstr(key+1)
	node  = hashEntry(key,data)
	pos = f(key)
	tabla.slot[pos]
	tabla.insertElem(node)



