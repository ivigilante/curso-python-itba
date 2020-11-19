# Paréntesis balanceados
# En este desafío deben programar un linter que verifique la correcta utilización de los paréntesis en un texto.

# La entrada del programa será un texto, que puede o no contener paréntesis (), corchetes [] y llaves {}, además de cualquier otra letra o símbolo. Su tarea es determinar que el texto sea válido, lo cual en este caso quiere decir que la utilización de paréntesis, corchetes y llaves es correcta, cada símbolo de apertura se corresponde con uno de cierre. Imprimir True o False si el texto es válido o no.

# Tips:

# Investigar el comportamiento de Pilas LIFO ya que son de extrema utilidad en este problema. Pueden utilizar listas de Python con los comandos append y pop para que se comporte como una pila LIFO.
# Sugerimos usar una estructura de datos para determinar las parejas de símbolos, el código será más sencillo y además será mucho más fácil agregar otras parejas de símbolos en el futuro. Algunas opciones posibles que se nos ocurrieron, aunque no las únicas, son:
# openers = ['(', '{', '[']
# closers = [')', '}', ']']
# brackets = {'(':')', '[':']', '{':'}'}
# Ejemplos:

# Cada paréntesis se cierra:

# esBalanceado( "Yo (Juan) quiero (necesito) café." ) => True
# Cada símbolo se cierra en el orden correcto:

# esBalanceado( " { 1-[ 2*( 3+4 ) ] } " ) => True
# Cada símbolo se cierra en el orden correcto:

# esBalanceado( " [ [1,2,3], [4,5,6], [7,8,9] ] " ) => True
# Falta cerrar el corchete ]:

# esBalanceado( " [1*(2+3) " ) => False
# Falta abrir la llave {:

# esBalanceado( " }[]() " ) => False
# Se cierran en el orden incorrecto, hay un ] entre los ( ):

# esBalanceado( " { [ ( ] ) } " ) => False

openers = ["(", "{", "["]
closers = [")", "}", "]"]

def esBalanceado(texto):
	pila = []
	for char in texto:
		if char in openers:
			pila.append(char)
		elif char in closers:
			if not(pila):
				return False
			elem = pila.pop()
			if char != closers[openers.index(elem)]:
				return False
	if pila:
		return False
	return True

esBalanceado("Yo (Juan) quiero (necesito) café.") # t
esBalanceado(" { 1-[ 2*( 3+4 ) ] } ") # t
esBalanceado( " [ [1,2,3], [4,5,6], [7,8,9] ] " ) # t
esBalanceado( " [1*(2+3) " ) # f
esBalanceado( " }[]() " ) # f
esBalanceado( " { [ ( ] ) } " ) # f