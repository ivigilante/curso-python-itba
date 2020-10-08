# Mini-desafio Operaciones de Modificacion
# Diseñar un programa en el cual el usuario ingrese tres números
# uno a la vez, y se muestre a la salida el promedio de los tres números.

def op_modificacion():
	num1 = int(input("Ingrese el 1er numero: "))
	num2 = int(input("Ingrese el 2do numero: "))
	num3 = int(input("Ingrese el 3er numero: "))
	prom = (num1 + num2 + num3) /3
	print(prom)

# Mini-desafio Operador Modulo

# Realizar un programa al cual se ingresa el día del año mediante 
# un número de 0 a 364, y que muestra en pantalla a qué día de la semana corresponde mediante 
# un número de 0 a 6 (mostrar el número 0 si corresponde a Lunes y 6 si es Domingo)
# Suponemos que el día 0 del año cae un Lunes.

def op_modulo():
	dia = int(input("Ingrese el dia del anno: "))
	dia_de_la_semana = dia % 7
	# 0 = Lunes, 1 = Martes, 2 = Miercoles, 3 = Jueves, 4 = Viernes, 5 = Sabado, 6 = Domingo 
	print(dia_de_la_semana)

# Mini-desafio if

# A) Realizar un programa que revise si una nota está aprobada (es decir si es mayor o igual a 4) 
# utilizando un if/else. La nota será ingresada por el usuario usando input().
# B) Realizar un programa que convierta una nota porcentual del 0 al 100 
# a una letra entre A y F de acuerdo a la siguiente conversión:

#A: 90–100
#B: 80–89
#C: 70–79
#D: 60–69
#F: 0–59

def desafio_if_a():
	nota = int(input("Ingrese la nota a evaluar: "))
	if nota >= 4:
		print("Aprobado")
	else:
		print("Desaprobado")

def desafio_if_b(): 
	nota = int(input("Ingrese la nota a evaluar: "))
	if 90 <= nota and nota <= 100:
		print("A")
	if 80 <= nota and nota <= 89:
		print("B")
	if 70 <= nota and nota <= 79:
		print("C")
	if 60 <= nota and nota <= 69:
		print("D")
	if 0 <= nota and nota <= 59:
		print("F")

# Mini-desafío If y While

# Implementar un programa que muestre la siguiente secuencia:
# 1, 2, 3, 4, 5, 4, 3, 2, 1, 0
# Para un desafío mayor: Utilizar un solo while, un solo if y un solo else

def desafio_if_while():
	i = 1
	while(i <= 10):
		if i < 5:
			print(i)
		else:
			print(10-i)
		i+=1

# Mini-desafío for

# Mostrar la siguiente secuencia de datos utilizando la instrucción for y la instrucción if:
# 0, 1, 4, 9, 16, 25, 6, 7, 8, 9
# 0 -> 1 d1 i * 2 + 1 = 0 * 2 + 1
# 1 -> 4 d3 = 1 * 2 + 1
# 4 -> 9 d5 = 2 * 2 + 1 // + 4 o + 5
# 9 -> 16 d7 = 3 * 2 + 1 // + 9 o + 8
# 16 -> 25 d9
# 25 -> 6 
# 6 -> 7 
# 7 -> 8
# 8 -> 9

def desafio_for():
	for i in range(10):
		if i > 5:
			print(i)
		else:
			print(i**2)

# Mini-desafío funciones

# Escribir una función que chequee los siguientes usuarios y contraseñas:
# Usuario: Juan - Contraseña: 12345_
# Usuario: Pablo - Contraseña: xDcFvGbHn
# La función debe recibir como parámetros el usuario y la contraseña, y debe 
# devolver el valor True o False.

def desafio_func(usuario, password):
	if usuario == "Juan" and password == "12345_":
		return True
	if usuario == "Pablo" and password == "xDcFvGbHn":
		return True
	return False

# Un menu sencillo para testear mini-desafios:
end_program = False
while(not(end_program)):
	print("Mini desafios de la clase 1:")
	print("1. Operaciones de modificacion")
	print("2. Operador Modulo")
	print("3. Estructura IF")
	print("4. Estructura WHILE")
	print("5. Estructura FOR")
	print("6. Funciones")
	print("7. Salir")

	opcion = int(input("> "))
	if opcion == 1:
		op_modificacion()
	if opcion == 2:
		op_modulo()
	if opcion == 3:
		print("1. Desafio Nota aprobada")
		print("2. Desafio Nota Porcentual -> Nota Alfabetica")
		opcion_desafio_if = int(input("> "))
		if opcion_desafio_if == 1:
			desafio_if_a()
		if opcion_desafio_if == 2:
			desafio_if_b()
	if opcion == 4:
		desafio_if_while()
	if opcion == 5:
		desafio_for()
	if opcion == 6:
		# Imprimo usuarios registrados para que sea mas facil...
		print("Usuarios registrados:")
		print("\tUser: Juan")
		print("\tPass: 12345_\n")
		print("\tUser: Pablo")
		print("\tPass: xDcFvGbHn\n")
		user = input("Ingrese usuario: ")
		password = input("Ingrese password: ")
		if desafio_func(user, password):
			print("Login Successful")
		else:
			print("Login Failed")
	if opcion == 7:
		print("Finalizando programa!")
		end_program = True





