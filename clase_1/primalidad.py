# Test de primalidad
# Escribir una función que recibe un numero y devuelve True si 
# el numero es primo y False en caso contrario.
# Mediante un for verificar la primalidad de los numeros del  1  al  20 .
# Tips
# Un número  𝑁  es primo cuando tiene exactamente  2  divisores ( 1  y  𝑁 ).
# Sin embargo alcanza con verificar que no es múltiplo de ningún 
# número entre  2  y  𝑁‾‾√  (recordar que  𝑁‾‾√=𝑁0.5 )
# El numero 1 no es primo.
def esPrimo(n):
	if n == 1 or n == 0:
		return False
	for i in range(2,int(n**0.5)+1):
		if n % i == 0:
			return False
	return True

def testPrimalidad():
	for i in range(1,21):
		if esPrimo(i):
			print(str(i) + " es primo.")
		else:
			print(str(i) + " no es primo.")