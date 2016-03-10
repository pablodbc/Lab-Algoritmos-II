from cuco_htable import *
from random import *
from string import *
from sys import *

def checkSize(valorEsperado, valorReal):
	if valorReal == valorEsperado:
		print "Tabla inicializada correctamente"
	else:
		print "Tabla no inicializada correctamente"
def randomstr(N):
	return ''.join(choice(lowercase) for i in range(N))
def checkInsert(tabla):
	key = randint(0,2*tabla.size)
	data = randomstr(key+1)
	pos1 = f1(key,tabla)
	pos2 = f2(key,tabla)
	tabla.insert(key,data)
	i = tabla.slot[pos1]
	j = tabla.slot[pos2]
	if (i!=None and i.data == data and i.key == key) or (j!=None and j.data == data and j.key == key):
		print "La funcion insert es correcta"
	else:
		print "La funcion insert no es correcta"

def checkDelete(tabla):
	key = randint(0,2*tabla.size)
	data = randomstr(key+1)
	pos1 = f1(key,tabla)
	pos2 = f2(key,tabla)
	tabla.insert(key,data)
	i = tabla.slot[pos1]
	j = tabla.slot[pos2]
	tabla.delete(key)
	k = tabla.slot[pos1]
	l = tabla.slot[pos2]
	if (i!=None and k == None) or (j!=None and l == None):
		print "La funcion delete funciona correctamente"
	else:
		print "La funcion delete no funciona correctamente"
def checkSearch(tabla):
	key = randint(0,2*tabla.size)
	s = tabla.search(key)
	i = tabla.slot[f1(key,tabla)]
	j = tabla.slot[f2(key,tabla)]	

	if s == None:
		if s == j or s == i:
			print "La funcion Search funciona correctamente"
		else:
			print "La funcion Search no funciona correctamente"
	else:
		if s == j.data or s == i.data:
			print "La funcion Search funciona correctamente"
		else:
			print "La funcion Search no funciona correctamente"

def probarTabla(n):
	tabla = cucoTable(n)
	checkSize(n,len(tabla.slot))
	checkInsert(tabla)
	checkDelete(tabla)
	checkSearch(tabla)
	print
	print "Llenando tabla con elementos al azar..."
	for i in range(20):
		tabla.insert(i,randomstr(i+1))
	print
	print "Imprimiendo tabla..."
	print tabla
if __name__ == "__main__":
	probarTabla(int(argv[1]))