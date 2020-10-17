# Call me  ∂∂𝑥 , or  diff  for short
# Una operacion muy comun al manejar datos es la derivada

# 𝑑𝑑𝑡(Datos) 

# Escribir una función que reciba una lista de números. 
# Llamemos  𝑛  a la cantidad de elementos en esta lista. 
# Debe devolver una lista de tamaño  𝑛−1  con los 
# valores de la derivada discreta de la lista recibida.

# La derivada discreta corresponde a la diferencia 
# entre un elemento y su anterior, podemos usar la 
# siguiente definición:

# derivada[𝑖]=𝑥[𝑖+1]−𝑥[𝑖]

def derivada(lista_numeros):
	derivada_discreta = []
	for i in range(len(lista_numeros)-1):
		derivada_discreta.append(lista_numeros[i+1] - lista_numeros[i])
	return derivada_discreta
print(derivada([18,5,8,12]))