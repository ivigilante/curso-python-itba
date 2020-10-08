# Una buena e-stimación
# El número  𝑒  tiene inmensa utilidad para el análisis y la 
# estadística, es una de las super-estrellas de la matemática, y 
# su utilidad radica en que la función  𝑒^𝑥  es igual a su 
# derivada, por definición de  𝑒 .
# Gracias a las series de Taylor podemos obtener la siguiente 
# definición del número  𝑒 :
# 𝑒=1+1/1!+1/2!+1/3!+1/4!+1/5!+... 
# Se pide obtener una aproximación del número  𝑒  
# 3calculando la suma de los primeros  20  términos de esta sucesión infinita.
# Tips
# 𝑛!=1⋅2⋅3⋅ ... ⋅𝑛 .
# No voy a usar math.factorial asi hago mi propia funcion factorial(n)
def factorial(n): # Con recursion
	if n == 1:
		return n
	else:
		resultado = n * factorial(n-1)
	return resultado

def factorialV2(n): # Sin recursion (mejor)
	fact = 1
	for i in range(1, n + 1):
		fact = fact * i
	return fact

def aproxE():
	e = 1
	for i in range(1,20):
		e += 1/factorialV2(i)
	return e