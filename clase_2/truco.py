# Quiero Retruco
# El Truco es un juego de cartas muy popular en Argentina. Se suele jugar con naipes españoles de 40 cartas, las cuales tienen 4 palos (basto, oro, espada y copa) y 10 números, 1,2,3,4,5,6,7,10,11 y 12. Si bien en esta ocasión no vamos a programar un juego de truco, sí vamos a resolver uno de los problemas más usuales que surgen cuando jugamos, el cual es definir qué carta gana y qué carta pierde cuando hay un duelo entre dos cartas.

# Esquema de hierarquia de cartas para el juego truco argentino
# En la imagen podemos observar el orden de importancia de las cartas de izquierda a derecha. El 1 de espada es la más importante (y por lo tanto siempre gana) mientras que los 4s son las cartas de menor importancia (casi siempre pierden). Las cartas en la misma columna empatan si se enfrentan.

# Programar una función con dos inputs tipo string carta A y carta B que retorne la carta ganadora (tipo string), o "empate" en caso de que lo haya. Ejemplos de como debería funcionar
#    dueloDeCartas("1 de espada", "1 de basto")
#    >>> 1 de espada
#    dueloDeCartas("7 de oro", "5 de oro")
#    >>> 7 de oro
#    dueloDeCartas("11 de copa", "11 de espada")
#    >>> empate
palos = ["espada","basto","copa","oro"]
cartas = {}
for palo in range(4):
	for numero in range(1,11):
		importancia = numero - 3
		if numero <= 3:
			importancia += 10
		if numero >= 8:
			numero += 2
		carta = str(numero) + " de " + palos[palo]
		if palos[palo] == "espada":
			if numero == 1:
				importancia = 14
			elif numero == 7:
				importancia = 12
		if palos[palo] == "oro":
			if numero == 7:
				importancia = 11
		if palos[palo] == "basto":
			if numero == 1:
				importancia = 13
		cartas[carta] = importancia

# def dueloDeCartas(carta1, carta2):
# 	if cartas[carta1] > cartas[carta2]:
# 		print(carta1)
# 	elif cartas[carta1] < cartas[carta2]:
# 		print(carta2)
# 	else:
# 		print("empate")

# dueloDeCartas("1 de espada", "1 de basto")
# dueloDeCartas("7 de oro", "5 de oro")
# dueloDeCartas("11 de copa", "11 de espada")

# Usar un diccionario donde la clave sea el nombre de la carta, y su contenido su importancia (un tipo int). Aprovechen la instrucción for para evitar tener que cargar todas las cartas una por una.

# A veces se suele jugar al truco con más de dos jugadores. Podría ocurrir duelos en los que participan  𝑛  cartas. Programar una función cuyo input sea una lista de strings con todas las cartas y retorne la ganadora. (En caso de empate que retorne alguna de las ganadoras, o una lista con las ganadoras). Ejemplos de como podría funcionar:
#  dueloDeCartas(["7 de basto","7 de espada","12 de espada", "4 de espada"])
#  >>> "7 de espada"
#  dueloDeCartas(["4 de espada","7 de basto","7 de copa", "5 de copa"]) #también podría haber dado 7 de basto 
#  >>> "7 de copa"

def dueloDeCartas(lista):
	cartas_altas = [] # Puede haber más de una
	lista.sort(key = cartas.get, reverse = True)
	cartas_altas.append(lista[0])

	for carta in lista[1:]:
		if cartas[carta] != cartas[lista[0]]:
			break
		cartas_altas.append(carta)

	if len(cartas_altas) > 1:
		print("Parda entre:")
	print(*cartas_altas, sep = " - ")

dueloDeCartas(["7 de basto","7 de espada","12 de espada", "4 de espada"])
dueloDeCartas(["4 de espada","7 de basto","7 de copa", "5 de copa"]) 
