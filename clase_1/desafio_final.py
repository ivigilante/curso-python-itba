# La conjetura del Dr. Lothar

# Escriba un programa que reciba un numero del usuario y repita el siguiente
# proceso usando un while:
# Si el numero es par, se debe dividir por  2 .
# Si el numero es impar, se debe multiplicar por  3  y sumar  1 .
# Este proceso se repite hasta llegar al numero  1  y 
# luego muestra en pantalla la cantidad de pasos que tardó en llegar.

# Ejemplo para  𝑛=6 :
# 6,3,10,5,16,8,4,2,1 
# Resultado = 8

# Para un desafío mayor: Resolver el problema aplicando 
# funciones con recursión.

# Dato extra:
# En 1937, Lothar Collatz conjeturó que este proceso llega a 1 sin importar el número en el cual se empieza, pero hasta el día de hoy no se pudo demostrar su conjetura. Ya se comprobó usando programas de computadora que esto es verdad para todos los numeros menores que  258 

def lothar(n, n_pasos = 0):
	if n == 1:
		return n_pasos
	else:
		n_pasos += 1
		if n % 2 == 0:
			n = n / 2
		else:
			n = n * 3 + 1
		return lothar(n,n_pasos)

n = int(input("Ingrese un numero: "))
print(lothar(n))

# Resuelto sin recursion:
# n_pasos = 0
#
# while n != 1:
# 	n_pasos += 1
# 	if n % 2 == 0:
# 		n = n / 2
# 	else:
# 		n = n * 3 + 1
# 	print(n)
# print(n_pasos)