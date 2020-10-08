# Locos por las matemáticas

# En marzo 2019, Emma Haruka Iwao, una empleada de Google, 
# logró calcular 31,4 trillones de dígitos del famoso número pi en 121 dias 
# usando el poder de la nube de Google. ¡Hoy ustedes pueden hacer lo mismo con la ayuda de Python!
# Aprovechando el descubrimiento del matemático indio 
# Sriniviasa Ramanujan (1910) podemos emplear nuestro propio aproximador de pi.
# 1𝜋=22‾√9801∑𝑘=0∞(4𝑘)!⋅(1103+26390𝑘)(𝑘!)43964𝑘 
# Tips:
# Pueden utlizar la siguiente función para calcular factoriales:
# def factorial(n):
#   return 1 if n<=1 else n*factorial(n-1)
# factorial(4)=4!=24 
# Esto es un problema abierto. No es posible conseguir una 
# representación decimal exacta de  𝜋 , por lo tanto solo se puede estimar.
# Si no estamos tan locos por la matemáticas podemos usar 
# otras aproximaciones más simples como:
# 𝜋≈227≈355113 
# Otros números famosos:
def factorial(n):
	ans = 1
	for i in range(1,n+1):
		ans *= i
	return ans

def pi(n):
	sumatoria = 0
	for k in range(n):
		val1 = factorial(4*k) * (1103 + 26390 * k)
		val2 = (factorial(k))**4 * 396**(4*k)
		sumatoria += val1/val2
	pi_inv = ((2 * 2**0.5) / 9801) * sumatoria
	pi = 1/pi_inv
	return pi
def num_e(n):
	sumatoria = 0
	for i in range(n):
		sumatoria += 1/factorial(i)
	return sumatoria
def phi():
	return (1 + 5**0.5)/2
print(pi(1000))
print(num_e(1000))
print(phi())
