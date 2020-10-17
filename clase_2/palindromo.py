#  ¿Acaso hubo buhos aca?
# Definir una función que detecte si 
# una palabra es un palíndromo y devuelve True o False.

# Ejemplos:

# palindromo( "python" ) => False

# palindromo( "reconocer" ) => True

# palindromo( "Neuquén" ) => False

# ★★  Challenge: Modificar la función para 
# ignorar espacios, signos de puntuación, y que 
# no haga distinción entre mayúsculas y minúsculas 
# (pueden usar str.lower). Sugerimos usar el nombre 
# del desafío como un palindromo de ejemplo.

def palindromo(palabra):
	palabra = "".join([letra for letra in palabra.lower() if letra.isalpha()])
	for i in range(len(palabra)//2):
		if palabra[i] != palabra[-(i+1)]:
			return False
	return True
