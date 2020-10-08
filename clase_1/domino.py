# Dominó
# El Dominó es un juego de mesa muy popular. En este ejercicio no vamos a 
# programar un juego de Domino, pero sí contar sus fichas.
# A pesar de que el domino tradicional se juega con fichas hasta el número 6
# vamos a considerar un juego de fichas de valor máximo  𝑛 .
# Escribir una función que calcule la cantidad de fichas para un juego 
# de dominó completo con fichas que contienen hasta el número  𝑛 . 
# Nota: ¡No hay fichas repetidas! 2-4 es la misma ficha que 4-2. 
# ¡Observar que en el dominó hay fichas con valor 0!
#    cantidadFichas(3)
#    >>> 10
#    cantidadFichas(4)
#    >>> 15

# Seguro hay una forma mejor, con una formula, pero no la pude pensar
# def cantidadFichas(valorMaximo):
#    # Si el valor maximo es 3, las fichas son 0,1,2,3 (4 posibilidades)
#    posibilidades = valorMaximo + 1
#    cant_de_fichas = posibilidades * posibilidades
#    cant_de_fichas_sin_repeticiones = cant_de_fichas
#    for i in range(posibilidades):
#       cant_de_fichas_sin_repeticiones -= i
#    print(cant_de_fichas_sin_repeticiones)
# Con formula:
def cantidadFichas(valorMaximo):
   posibilidades = valorMaximo + 1
   cant_fichas = int((posibilidades * (posibilidades + 1) ) /2)
   print(cant_fichas)
# Escribir una función que muestre todas las fichas para 
# un juego de dominó como el anterior, en cualquier orden.
#    mostrarFichas(3)
#    >>> 0-0
#    >>> 0-1
#    >>> 0-2
#    >>> 0-3
#    >>> 1-1
#    >>> 1-2
#    >>> 1-3
#    >>> 2-2
#    >>> 2-3
#    >>> 3-3
def mostrarFichas(valorMaximo):
   for i in range(valorMaximo+1):
      for j in range(valorMaximo+1):
         if j >= i:
            print(str(i) + "-" + str(j))

# Llamar a las funciones anteriores con distintos valores 
# para corroborar su funcionamiento
print("cantidadFichas(3)")
cantidadFichas(3)
print("cantidadFichas(4)")
cantidadFichas(4)
print("mostrarFichas(3)")
mostrarFichas(3)

# Challenge: Escribir una función que, 
# dada una cantidad de fichas, calcule cuál es el  𝑛  (valor máximo) 
# de las fichas. Si el número de fichas no corresponde a 
# la cantidad de fichas de ningún juego de dominó 
# completo retornar -1.
   # valorMaximo(10)
   # >>> 3
   # valorMaximo(11)
   # >>> -1
   # valorMaximo(15)
   # >>> 4
def valorMaximo(cantFichas):
   serie = ((((8*cantFichas+1)**0.5) -1) /2) -1
   if serie.is_integer() and serie > 0:
      print(serie)
   else:
      print("-1")
valorMaximo(10)
valorMaximo(11)
valorMaximo(15)
