# Dr. Chaos, el malevolo semiótico
# "Chaos es caos en inglés" te diría Dr. Chaos, charlando con una taza de té Chai en la mano. En verdad no es tán malo como su nombre lo hace aparentar... si es que tenés un buen manejo de los idiomas.

# Dr. Chaos esta armando un diccionario. Este diccionario tiene la particularidad de no tener definiciones; el diccionario de Dr. Chaos define una palabra como otra. Dr. Chaos quiere comenzar a traducir la literatura de todo el mundo usando el diccionario y ha venido a ti, el Number One programador de Python.

# Objetivo: Cambiar las palabras de una oración usando el diccionario de Dr. Chaos e imprimir la nueva oración en el lenguaje unificado.

# Ejemplo:

# diccionario = {"hola":"你好","como":"how","estás":"estáis"}

# oracion = "hola, como estás?"

# OUTPUT: "你好, how estáis?"

# Ejemplo 2:

# diccionario = {"ve":"regards","bien":"bom","se":"it"}

# oracion = "se ve bien!"

# Tips:

# El programa debería tratar los símbolos de interrogación, exclamación, los puntos y comas como whitespace, es decir, espacio en blanco.

# Suponer que las letras son todas minusculas.

diccionario = {"hola":"你好","como":"how","estás":"estáis","ve":"regards","bien":"bom","se":"it"}
oracion = "hola, como estás?"
oracion2 = "se ve bien!"

def traducir(texto):
	word = ""
	traduccion = ""
	for char in texto:
		if char.isalpha():
			word += char
		else:
			traduccion += diccionario.get(word,"") + char
			word = ""
	return traduccion

print(traducir(oracion))
print(traducir(oracion2))