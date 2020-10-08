# Ejercicio de entrevista en Ingemática
# Escriba un programa que imprima los números del 1 al 100, 
# pero que para cada número que sea múltiplo de 3 imprima N3, 
# para los múltiplos de 5 imprima N5, y para los múltiplos de los dos, N3N5.
# Tips
# ¡Si el número es divisible por 3 entonces el resto de la división vale cero!
def entrevistaIngematica():
	for i in range(1,101):
		str = ""
		if i % 3 == 0:
			str += "N3"
		if i % 5 == 0:
			str += "N5"
		if str:
			print(str)
		else:
			print(i)