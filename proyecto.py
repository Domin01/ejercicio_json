from funciones import *
import json

with open('regiones.json') as file:
    regiones = json.load(file)



menu='''
1.-Dime el nombre de todas las regiones.
2.-Cuenta el numero de regiones.
3.-
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
		print(menu)
		opcion=int(input("Elige una opcion: "))
	
	if opcion==2:
		print(f"Existen un numero de {ContarRegiones(regiones)} regiones")
		print(menu)
		opcion=int(input("Elige una opcion: "))

	if opcion== 6:
		break

#Los diccionarios python tienen un par de métodos que pueden serte útiles en este caso. 
#diccionario.keys() te da una lista con todas las claves del diccionario. diccionario.items() 
#te da otra lista con parejas (clave, valor).

#Usando ambas cosas y el método str.join() para concatenar varios elementos de una lista 
#y formar con ellos una cadena, puedes hacer lo siguiente:

#Dime el nombre de todas las regiones

