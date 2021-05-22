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

def FiltrarRegiones(regiones,busqueda):
    nombre=[]
    for clave, valor in regiones.items():
        if valor["name"].startswith(busqueda):
            nombre.append(valor["name"])
    return nombre

def InfoRegion(regiones,busqueda):
    nombre=[]
    for clave, valor in regiones.items():
        if valor["name"].startswith(busqueda):
            nombre.append(valor["name"])
            nombre.append(valor["name_tr"])
            nombre.append(valor["continent"]["code"])
            nombre.append(valor["continent"]["name"])
    return nombre
