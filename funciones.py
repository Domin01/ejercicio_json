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