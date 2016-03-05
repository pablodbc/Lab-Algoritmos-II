from hashEntry import *
from hash_table import *
from dlist import *
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
def checkInsertNode(tabla):
	key = randint(0,2*tabla.size)
	data = randomstr(key+1)
	node  = hashEntry(key,data)
	pos = f(key,tabla)
	tabla.insertNode(node)
	j = tabla.slot[pos].search(key)
	if j == None:
		print "La funcion insertNode no funciona correctamente"
	else:
		print "La funcion insertNode funciona correctamente"
def checkInsert(tabla):
	key = randint(0,2*tabla.size)
	data = randomstr(key+1)
	pos = f(key,tabla)
	tabla.insert(key,data)
	j = tabla.slot[pos].search(key)
	if j == None:
		print "La funcion insert no funciona correctamente"
	else:
		if j.data == data:
			print"La funcion insert funciona correctamente"
		else:
			print "Error, se encontro la clave pero el string no corresponde al insertado"
def checkDeleteNode(tabla):
	key = randint(0,2*tabla.size)
	data = randomstr(key+1)
	pos = f(key,tabla)
	node = hashEntry(key,data)
	tabla.insertNode(node)
	tabla.deleteNode(node)
	j = tabla.slot[pos].search(key)
	if j == None:
		print "La funcion deleteNode funciona correctamente"
	else:
		print "La funcion deleteNode no funciona correctamente"
def checkDelete(tabla):
	key = randint(0,2*tabla.size)
	data = randomstr(key+1)
	pos = f(key,tabla)
	tabla.insert(key,data)
	tabla.delete(key)
	j = tabla.slot[pos].search(key)
	if j == None:
		print "La funcion delete funciona correctamente"
	else:
		print "La funcion delete no funciona correctamente"
def checkSearch(tabla):
	key = randint(0,2*tabla.size)
	s = tabla.search(key)
	j = tabla.slot[f(key,tabla)].search(key)
	if s == None:
		if s == j:
			print "La funcion Search funciona correctamente"
		else:
			print "La funcion Search no funciona correctamente"
	else:
		if s == j.data:
			print "La funcion Search funciona correctamente"
		else:
			print "La funcion Search no funciona correctamente"

def probarTabla(n):
	tabla = hashTable(n)
	checkInsertNode(tabla)
	checkInsert(tabla)
	checkDeleteNode(tabla)
	checkDelete(tabla)
	checkSearch(tabla)
	print "Imprimiendo tabla..."
	print tabla
if __name__ == "__main__":
	probarTabla(int(argv[1]))