# Convirtiendo números
# Después de usar tantas veces la instrucción int() para realizar conversiones, uno empieza a preguntarse ¿Será muy complicado convertir textos a números?

# Para poner esto a prueba, les proponemos crear su propio int(). Para lograrlo deben definir una funcion text2number() que reciba como parámetro una variable de tipo string y devuelva un número entero correspondiente a la conversión, tal como funciona int(). Los requisitos que debe cumplir la entrada para ser considerada válida son:

# Al inicio puede contener o no cierta cantidad de espacios ' '.
# Luego puede o no tener 1 caracter de signo: '+' ó '-'.
# Luego tiene cierta cantidad de caracteres numéricos: entre '0' y '9'.
# Por último puede contener o no cierta cantidad de espacios ' '.
# Como buena práctica de programación, les recomendamos considerar diferentes casos límites para verificar que el código logra manejarlos adecuadamente, además de ejemplos válidos también comprobar donde las condiciones no se cumplen o estan en el límite de cumplirse. De esa forma pueden asegurarse de que su código hace lo que esperaban en todo tipo de situaciones.

# Quedará a su criterio definir lo que hace la función cuando la entrada no se considera válida.

# Tips:

# Al igual que las listas, los strings son "iterables". Los tipos de datos "iterables" permiten entre otras cosas realizar un for que recorre todos sus elementos:

# texto = "Hola Mundo!"
# for letra in texto:
#   print(letra)
# Para obtener el valor numérico de 1 sólo caracter comprendido entre '0' y '9' pueden definir un diccionario como el siguiente:

# numeros = {'0':0, '1':1, '2':2, '3':3, '4':4, '5':5, '6':6 '7':7, '8':8 , '9':9}

# Una alternativa más sofisticada involucra el llamado código ASCII, y se relaciona con la forma en la cual los caracteres son representados en la memoria. Usando el comando ord() se obtiene el código ASCII de un caracter, y restando ord('0') se obtiene el valor numérico de un caracter entre '0' y '9':

# caracter = '5'
# numero = ord(caracter) - ord('0')
def text2number2(texto):
	texto.strip()
	print(texto)
	texto_num = texto.strip()
	num = 0
	positivo = True
	if texto_num[0] == "-" or texto_num[0] == "+":
		positivo = texto_num[0] == "+"
		texto_num = texto_num[1:]
	for char in texto_num:
		if "0" <= char <= "9":
			num = num * 10 + ord(char) - ord("0")
		else:
			return None
	return num if positivo else -num

def text2number(texto):
	negativo = False
	num = 0
	while texto.startswith(" "):
		texto = texto[1:]
	while texto.endswith(" "):
		texto = texto[:-1]

	if texto[0] == "-" or texto[0] == "+":
		if texto[0] == "-":
			negativo = True
		texto = texto[1:]

	for char in texto:
		if "0" <= char and char <= "9":
			num = num * 10 + (ord(char) - ord("0"))
		else:
			return None

	if negativo:
		num *= -1 # podria hacer return -num
	return num

tex = "       123341             "
print(text2number2(tex))
print(tex)

# print(text2number("-98"))
# print(text2number("  +123   "))
# print(text2number("  -47 "))
# print(text2number("12s3"))

# print(text2number2("123"))
# print(text2number2("-98"))
# print(text2number2("+98"))

# print(text2number2("  +123   "))
# print(text2number2("  -47 "))
# print(text2number2("12s3")) 