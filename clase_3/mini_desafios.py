# Leer el archivo Tabla1.xlsx que contiene los puntos de un campeonato. 
# El archivo tiene dos columnas, Equipo y Puntos. 
# Determinar de cada equipo la diferencia de gol 
# (goles a favor - goles en contra), y mostrar todas las diferencias de gol con print

import pandas

def dif_goles():
	archivo = pandas.read_excel("Tabla1.xlsx", index_col = "Equipo")
	archivo = archivo.to_dict("index")
	for equipo, puntos in archivo.items():
		print("{}: {}".format(equipo, puntos["Goles a favor"] - puntos["Goles en contra"]))
#dif_goles()

# Leer el archivo Tabla1.xlsx que contiene los puntos de un campeonato y determinar qué equipo es el campeón (1ro) y perdedor (último). El archivo tiene dos columnas, Equipo y Puntos
def campeon():
	archivo = pandas.read_excel("Tabla1.xlsx", index_col = "Puntos")
	archivo = archivo.to_dict("index")
	print(archivo)
	print(archivo.keys())
	print("Ganador:",archivo[max(archivo.keys())]["Equipo"])
	print("Perdedor:",archivo[min(archivo.keys())]["Equipo"])
# campeon()

# Calcular el promedio de las notas de química de todos los alumnos en el archivo Datos.xlsx.

def prom_materia(materia):
	archivo = pandas.read_excel("Datos.xlsx")
	archivo = archivo.to_dict("list")
	promedio = round(sum(archivo[materia]) / len(archivo[materia]),2)
	print(promedio)
# prom_materia("Quimica")

# Escribir una funcion que reciba como parámetros: una variable de tipo DataFrame (la tabla de alumnos) y el índice de un alumno. Luego debe devolver con return el promedio de sus notas en las diferentes materias.

def notas_alumno(dataframe, idx): # Usando records y listas
	datos = dataframe.to_dict("records")
	print("Notas de: {} {}".format(datos[idx]["Nombre"], datos[idx]["Apellido"]))
	for materia, nota in list(datos[idx].items())[3::]:
		print(materia,": " ,nota)
	# Promedio de toda sus materias
	prom = round(sum([nota for materia, nota in list(datos[idx].items())[3::]]) / len (list(datos[idx].keys())[3::]),2)
	print(prom)
def notas(dataframe, idx): # Usando dataframe
	print("Notas de {} {}".format(dataframe.loc[idx]["Nombre"],dataframe.loc[idx]["Apellido"]))
	
	for materia, nota in dataframe.loc[idx].drop(index = ["Nombre", "Apellido", "Legajo"]).items():
		print(materia,": ",nota)

	notas = [nota for nota in dataframe.loc[idx][3::]]
	promedio = round(sum(notas) / len(notas), 2)
	print("Promedio total:",promedio)
# archivo = pandas.read_excel("Datos.xlsx")
# notas(archivo, 3)

def prom_general(dataframe, idx):
	print("Notas de {} {}".format(dataframe.loc[idx]["Nombre"],dataframe.loc[idx]["Apellido"]))
	notas = [nota for nota in dataframe.loc[idx][3::]]
	promedio = round(sum(notas) / len(notas), 2)
	print("Promedio total:",promedio)

# Obtener el promedio general sólo para aquellos alumnos que aprobaron Matematica.
def prom_si_aprobaron(materia):
	datos = pandas.read_excel("Datos.xlsx")
	datos = datos[datos[materia] >= 4]
	for i in datos.index:
		prom_general(datos,i)
# prom_si_aprobaron("Matematica")

# Encontrar la cantidad de ocurrencias de la palabras "Trump" y "the" en el texto de la noticia.
def encontrar_palabras(archivo, palabras_buscadas):
	char_no_deseados = ('\ufeff', '—', '\n', '’s', ',', '.')
	file = open(archivo,"r")
	palabras = []
	contenido = file.readlines()
	for linea in contenido:
		for char in char_no_deseados:
			linea = linea.replace(char, "")
		palabras += [palabra.upper() for palabra in linea.split()]

	for palabra_buscada in palabras_buscadas:
		print("Se encontraron {} ocurrencias de la palabra \"{}\"".format(palabras.count(palabra_buscada.upper()), palabra_buscada))
# encontrar_palabras("noticia.txt", ["trump","the"])

# Encontrar la palabra con mayor numero de ocurrencias en el texto de la noticia.
def encontrar_mayor_repeticiones(archivo):
	char_no_deseados = ('\ufeff', '—', '\n', '’s', ',', '.')
	file = open(archivo,"r")
	palabras = []
	contenido = file.readlines()
	for linea in contenido:
		for char in char_no_deseados:
			linea = linea.replace(char, "")
		palabras += [palabra.upper() for palabra in linea.split()]

	palabras_contadas = []
	mayor_repeticion = {"palabra":"", "repeticiones":0}
	for palabra in palabras:
		if palabra not in palabras_contadas:
			repeticiones = palabras.count(palabra)
			palabras_contadas.append(palabra)
			if repeticiones > mayor_repeticion["repeticiones"]:
				mayor_repeticion["palabra"] = palabra
				mayor_repeticion["repeticiones"] = repeticiones
	print("La palabra con mayor repeticiones es \"{}\" con {} repeticiones".format(mayor_repeticion["palabra"],mayor_repeticion["repeticiones"]))
# encontrar_mayor_repeticiones("noticia.txt")