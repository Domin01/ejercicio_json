# EJERCICIO JSON
#### A partir del fichero vuln.xml obtener la siguiente información:
* **Listar la información:** Dime el nombre de todas las regiones en español y en su idioma
* **Contar la información:** Muestra la cantidad de farmacias de las que tenemos información.
* **Buscar o filtrar información:** Mostrar las farmacias de una localidad dada.
* **Buscar información relacionada:** Muestra las farmacias cuyo número de teléfono comience por un dato introducido.
* **Ejercicio Libre:** Mostrar el correo, horario, teléfono y localización a través de OpenStreetMap a través del nombre de las farmacias.

nombres=[]
for b in iniciales:
	for c in regiones:
		nombres.append(c[b]["name"])
		print(c)

for d in nombres:
	print(d)
print("hola",end="")