# Mini-desafío: floats
# Crear:
# Una función que convierta grados Celsius 
# a grados Farenheit (https://es.wikipedia.org/wiki/Grado_Fahrenheit)

# Una función que convierta grados Celsius 
# a grados Kelvin (https://es.wikipedia.org/wiki/Kelvin)

# El usuario debe ingresar una temperatura en grados 
# Celsius y el programa debe mostrar las conversiones 
# a Farenheit y Kelvin utilizando las funciones. 
# Si la temperatura ingresada es inferior al cero absoluto, 
# el programa debe mostrar un mensaje de advertencia.
# Pueden leer aqui sobre como hacer las conversiones.

# Cero absoluto = 0 Kelvin

def CelsiusToFarenheit(celsius):
	return celsius * 9/5 + 32
	
def CelsiusToKelvin(celsius):
	return celsius + 273.15

def desafio_floats():
	celsius = float(input("Ingrese temperatura en Celisu (ºC): "))
	print(CelsiusToFarenheit(celsius))
	kelvin = CelsiusToKelvin(celsius)
	print(kelvin)
	if kelvin <= 0:
		print("Cero absoluto alcanzado!")
# Mini-desafío: Operaciones con strings
# Hacer un programa que permita ingresar un nombre y 
# un apellido usando dos veces la función input( ). 
# Luego debe crear la variable nombre_y_apellido que contenga 
# ambos datos separados por un espacio. Un fabricante de tarjetas 
# admite la impresión de hasta 26 caracteres para el 
# nombre del dueño de la tarjeta, el programa debe 
# imprimir "Nombre admitido" si nombre_y_apellido cumple 
# con esta restricción y "Nombre no admitido" en caso contrario 
# (el espacio cuenta como uno de los 26 caracteres disponibles).

# Para un desafío mayor: Si nombre_y_apellido cumple la 
# restricción, mostrar el nombre y apellido. En caso contrario 
# nombre_y_apellido debe valer la inicial del nombre y 
# luego el apellido separado por un espacio. Si todavía no se cumple 
# la restricción entonces el valor será la inicial del nombre y 
# las primeras 24 letras del apellido. Mostrar el nombre resultante.

def operaciones_string():
	nombre = input("Nombre: ")
	apellido = input("Apellido: ")
	nombre_y_apellido = nombre + " " + apellido
	if (len(nombre_y_apellido) > 26):
		nombre_y_apellido = nombre[0] + " " + apellido
	if (len(nombre_y_apellido) > 26):
		nombre_y_apellido = nombre[0] + " " + apellido[0:24]

	print(nombre_y_apellido)

# Mini-desafío: listas
# 1. Crear una lista con los números pares menores a 50.

# 2. Crear una lista con el nombre de los días de la semana. Realizar un programa
# al cual se ingresa el día del año mediante un número de 0 a 364, que
# determine a qué día de la semana corresponde mediante un número de 0 (Lunes)
# a 6 (Domingo) y luego muestre en pantalla el elemento correspondiente de la
# lista, o sea, el día de la semana en forma de texto (suponemos que el día 0
# del año es Lunes).

# Ejemplos:
# calcularDia(1) => 'Martes' (Ya que el día 0 es Lunes)
# calcularDia(10) => 'Jueves' (Ya que el día 7 también es Lunes)

# 3. Realizar un programa que ordena nombres alfabeticamente. Primero debe pedir al usuario que ingrese el número de nombres que serán ingresados, luego debe pedir al usuario que ingrese un nombre y repetir ese pedido la cantidad de veces indicada. Los nombres se deben ir agregando a una lista. Por último, ordenar la lista alfabéticamente y mostrar en pantalla de a uno por vez los nombres ordenados (usando un for).

def desafio_listas1():
	lista = []
	for i in range(50):
		if i % 2 == 0:
			lista.append(i)
	return lista

def desafio_listas2():
	dias_de_la_semana = ["Lunes","Martes","Miercoles",
	"Jueves","Viernes","Sabado","Domingo"]

	dia = int(input("Ingrese dia (0-364): "))
	dia_de_la_semana = dia % 7
	print(dias_de_la_semana[dia_de_la_semana])

def desafio_listas3():
	nombres = [input("Nombre: ") for i in range(int(input("Ingrese cantidad de nombres: ")))]
	nombres.sort()
	print(nombres)

# Mini-desafío: Diccionarios
# Realizar un programa que pida al usuario un número de legajo y el nombre
# completo, luego lo guarde en un diccionario.

# Usar dos celdas de codigo, en una crear el diccionario, y en la otra agregar 
# el nombre y legajo, mostrar el contenido. La idea es que cuando se ejecute
# varias veces la segunda celda se agrege un nuevo nombre y legajo a lo que ya
# había sido almacenado en el diccionario.

def desafio_diccionarios():
	dic = {}
	for i in range(3):
		legajo = input("Ingrese legajo: ")
		nombre = input("Ingrese nombre completo: ")
		dic[legajo] = nombre
	print(dic)

# Para un desafío mayor: Mini-desafío: Diccionario²
# Se recibieron distintos postulantes para un empleo de traductor. Crear un 
# diccionario en el cual la clave de cada elemento sea el nombre de un
# candidato y el contenido sea un diccionario de los idiomas que aprendió.
# Para armar el diccionario de idiomas de cada candidato, los elementos deben 
# tener como clave el nombre del idioma y como contenido el valor True o False 
# para los siguientes idiomas: Español, Ingles, Chino, Frances, Italiano.

# Ejemplo del diccionario de idiomas:

# {"Español":True, "Ingles":True, "Chino":False, "Frances":False, 
# "Italiano":True}
# Inventar valores para 5 candidatos.

# El usuario luego debe poder ingresar el nombre de un idioma y el programa 
# deberá mostrar en pantalla el nombre de aquellos candidatos que aprendieron 
# ese idioma.

def desafio_mayor_diccionario():
	postulantes = {}
	dic_idiomas = {"Español":False, "Ingles":False, "Chino":False, "Frances":False, "Italiano":False}
	# Si quisiera hacer el input:
	# for i in range(5):
	# 	nombre = input("Ingrese nombre del postulante: ")
	# 	postulantes[nombre] = dic_idiomas.copy()
	# 	for idioma in dic_idiomas:
	# 		value = input("El postulante sabe {}? (s/n) ".format(idioma))
	# 		value = value.lower()
	# 		if value == "s":
	# 			postulantes[nombre][idioma] = True
	postulantes["Raul"] = {"Español":True, "Ingles":True, "Chino":False, "Frances":True, "Italiano":False}
	postulantes["Pedro"] = {"Español":True, "Ingles":False, "Chino":False, "Frances":False, "Italiano":False}
	postulantes["Ramiro"] = {"Español":True, "Ingles":True, "Chino":False, "Frances":False, "Italiano":True}
	postulantes["Norton"] = {"Español":False, "Ingles":True, "Chino":False, "Frances":True, "Italiano":False}
	postulantes["XiYuan"] = {"Español":False, "Ingles":True, "Chino":True, "Frances":False, "Italiano":False}

	idioma_buscado = input("Que idioma busca: ")
	for postulante in postulantes:
		if postulantes[postulante][idioma_buscado]:
			print(postulante)

# Mini-desafío: Sets
# Se cuentan con varios sets que contienen las personas que les gusta un 
# cierto sabor de helado:
# vainilla = { "Juan", "Marina", "Tomas", "Paula" }
# chocolate = { "Pedro", "Paula", "Marina" }
# dulceDeLeche = { "Juan", "Julian", "Pedro", "Marina" }
# Responder usando operaciones de sets:
# Hay alguna persona que le gusten todos los gustos?
# Hay alguna persona que le gusten la vainilla y no el dulce de leche?
# Cuantas personas distintas tenemos?
def desafio_sets():
	vainilla = { "Juan", "Marina", "Tomas", "Paula" }
	chocolate = { "Pedro", "Paula", "Marina" }
	dulceDeLeche = { "Juan", "Julian", "Pedro", "Marina" }

	# Hay alguna persona que le gusten todos los gustos?
	respuestaA = vainilla & chocolate & dulceDeLeche
	print("A {} le gustan todos los gustos.".format(respuestaA))
	# Hay alguna persona que le gusten la vainilla y no el dulce de leche?
	respuestaB = vainilla - dulceDeLeche
	print("A {} le gusta la vainilla, pero no el dulce de leche".format(respuestaB))
	# Cuantas personas distintas tenemos?
	respuestaC = vainilla | chocolate | dulceDeLeche
	print("Tenemos {} personas".format(len(respuestaC)))

