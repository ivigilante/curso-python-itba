# Aclaración: Este desafío es inventado, es posible que haya errores fácticos en cuanto a los alfabetos reales.

# Encontramos una piedra antigua en una plaza de Buenos Aires cuyas 
# inscripciones nos ayudan a decifrar nuevos alfabetos. Gracias a 
# estas inscripciones descubrimos que las letras del alfabeto 
# latino arcaico tienen una correspondencia con el alfabeto latino 
# y vamos a crear un programa que nos ayude a traducir palabras de un alfabeto a otro.

# Crear una función que recibe un string, transforma todos los caracteres del 
# alfabeto latino arcaico en caracteres modernos, no modifica el resto de 
# los caracteres (signos de puntuacion, espacios, etc.) y devuelve el resultado con return.

# Ejemplos:

# traducir( "𐌀𐌋𐌅𐌀𐌁𐌄𐌕𐌏" ) => "ALFABETO"

# traducir( "¡𐌐𐌄𐌓𐌃𐌉!" ) => "¡PERDI!

# traducir( "¿𐌔𐌉 𐌏 𐌍𐌏? 𐌌𐌌𐌌... 𐌔𐌉." ) => "¿SI O NO? MMM... SI."

# Correspondencia entre alfabetos:

# Arcaico : Moderno
# '𐌀' : 'A',
# '𐌁' : 'B',
# '𐌂' : 'C',
# '𐌃' : 'D',
# '𐌄' : 'E',
# '𐌅' : 'F',
# '𐌆' : 'Z',
# '𐌇' : 'H',
# '𐌉' : 'I',
# '𐌊' : 'K',
# '𐌋' : 'L',
# '𐌌' : 'M',
# '𐌍' : 'N',
# '𐌏' : 'O',
# '𐌐' : 'P',
# '𐌒' : 'Q',
# '𐌓' : 'R',
# '𐌔' : 'S',
# '𐌕' : 'T',
# '𐌖' : 'V',
# '𐌗' : 'X'

dic_traduccion = {
	'𐌀' : 'A',
	'𐌁' : 'B',
	'𐌂' : 'C',
	'𐌃' : 'D',
	'𐌄' : 'E',
	'𐌅' : 'F',
	'𐌆' : 'Z',
	'𐌇' : 'H',
	'𐌉' : 'I',
	'𐌊' : 'K',
	'𐌋' : 'L',
	'𐌌' : 'M',
	'𐌍' : 'N',
	'𐌏' : 'O',
	'𐌐' : 'P',
	'𐌒' : 'Q',
	'𐌓' : 'R',
	'𐌔' : 'S',
	'𐌕' : 'T',
	'𐌖' : 'V',
	'𐌗' : 'X'
}
# Usando translate
def traducirTranslate(string):
	translation_table = string.maketrans(dic_traduccion)
	print(string.translate(trans))

#Crear una función que recibe un string, transforma todos los caracteres del 
# alfabeto latino arcaico en caracteres modernos, no modifica el resto de 
# los caracteres (signos de puntuacion, espacios, etc.) y devuelve el resultado con return.
def traducir(string):
	list_caracteres = list(string)
	for i in range(len(list_caracteres)):
		if list_caracteres[i] in dic_traduccion:
			list_caracteres[i] = dic_traduccion[list_caracteres[i]]

	string = "".join(list_caracteres)
	print(string)

def traducirV2(string):
	for letra in string:
		if letra in dic_traduccion:
			string = string.replace(letra,dic_traduccion[letra])
	print(string)
traducir("𐌊𐌉𐌋𐌋 𐌕𐌇𐌄𐌌")
traducirTranslate("𐌊𐌉𐌋𐌋 𐌕𐌇𐌄𐌌")