from cuco_htable import *
from dlist import *
from hashEntry import *
from hash_table import *
from random import *
from sys import *
from string import *
from time import *
def probarTablas(m):
	datos = [randint(0,m)]*2000000
	ct = cucoTable(131071)
	ht = hashTable(131071)
	print "Comenzando prueba de Tabla de Hash Cuco..."
	t = time()
	for i in xrange(len(datos)):
		c = datos[i]
		if ct.search(c) == None:
			r = ct.insert(c,"CI2692")
			assert(r!=None)
		else:
			ct.delete(c)
	t = time() - t
	ctt=t
	print "Tiempo de ejecucion de Tabla de Hash Cuco", round(t,3)
	print
	print "Comenzando prueba de Tabla de Hash con encadenamiento..."
	t = time()
	for i in xrange(len(datos)):
		c = datos[i]
		if ht.search(c) == None:
			ht.insert(c,"CI2692")
		else:
			ht.delete(c)
	t = time() - t
	htt=t
	print "Tiempo de ejecucion de Tabla de Hash con encadenamiento", round(t,3)

	return (ctt,htt)

if __name__ == "__main__":
	thc = 0
	the = 0
	m = int(argv[1])
	for i in xrange(3):
		k = probarTablas(m)
		thc+=k[0]
		the+=k[1]

	print "Promedio Hashing cuco para",m,":",round(thc/3,3)
	print "Promedio Hashing con encadenamiento para",m,":",round(the/3,3)

