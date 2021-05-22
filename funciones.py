import json

#Dime el nombre de todas las regiones
def nombresregiones(regiones):
    nombre=[]
    nombrereal=[]
    lista=[]
    for clave, valor in regiones.items():
        nombre.append(valor["name"])
        nombrereal.append(valor["name_tr"])
    for listas in zip (nombre,nombrereal):
        lista.append(listas)
    return lista

def ContarRegiones(regiones):
    nombre=[]
    for clave, valor in regiones.items():
         nombre.append(valor["name"])
    return len(nombre)

def BuscarRegiones(regiones,busqueda):
    nombre=[]
    for clave, valor in regiones.items():
        if valor["continent"]["code"] == busqueda:
            nombre.append(valor["name"])
    return(nombre)

#Los diccionarios python tienen un par de métodos que pueden serte útiles en este caso. 
#diccionario.keys() te da una lista con todas las claves del diccionario. diccionario.items() 
#te da otra lista con parejas (clave, valor).

#Usando ambas cosas y el método str.join() para concatenar varios elementos de una lista 
#y formar con ellos una cadena, puedes hacer lo siguiente: