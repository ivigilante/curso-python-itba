# La leyenda de Filius Bonacci
# Espiral Fibonacci
# Imprima  𝑛  números de la sucesion de Fibonacci
# 0, 1, 1, 2, 3, 5, 8, 13, 21 ...
def fibonacci(n):
	n_anterior = 0
	n_actual = 1
	sucesion = ""
	for i in range(n):
		if i == 0:
			sucesion += "0"
		elif i == 1:
			sucesion += ", 1"
		else:
			aux = n_actual
			n_actual = n_actual + n_anterior
			n_anterior = aux
			sucesion += ", " + str(n_actual)
	print(sucesion)