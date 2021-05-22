from funciones import *
import json

with open('regiones.json') as file:
    regiones = json.load(file)



menu='''
1.-Dime el nombre de todas las regiones.
2.-Cuenta el numero de regiones.
3.-Buscar regiones por continentes.
4.-
5.-
6.-Salir 
'''

print(menu)
opcion=int(input("Elige una opcion: "))

while opcion!=6:

	if opcion==1:
		for info in nombresregiones(regiones):
			print(f"{info[0]} nombre en la region {info[1]}")
		opcion=int(input("Elige una opcion: "))
	
	if opcion==2:
		print(f"Existen un numero de {ContarRegiones(regiones)} regiones")
		opcion=int(input("Elige una opcion: "))
	
	if opcion==3:
		print("Listado de regiones:")
		busqueda=input("EU,AS,NA,SA,AF,AN,OC:")
		resultado=BuscarRegiones(regiones,busqueda)
		for a in resultado:
			print(a)
		opcion=int(input("Elige una opcion: "))

	if opcion== 6:
		break




