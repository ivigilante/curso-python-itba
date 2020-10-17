# Menta y Dulce de leche
# Introducción:

# Una de las muchas ventajas de los sets y los diccionarios es que permiten averiguar si contienen cierto elemento con gran velocidad, sin importar la cantidad de elementos que almacenan (esto se debe a que internamente utilizan una función hash). Acceder al valor asociado a cierta clave en un diccionario también es una operación muy veloz.

# En comparación, verificar si un elemento se encuentra dentro de una lista es lento, ya que el tiempo necesario es proporcional a la cantidad de elementos en la lista y para listas muy grandes con miles, millones o billones de elementos (como puede suceder en una base de datos) esto puede ser un problema importante. Sin embargo, una vez que se conoce el índice del elemento, acceder al elemento es una operación tan rápida como en un diccionario.

# Problema:

# Volviendo de hacer las compras en el supermercado, pasas cerca de una heladería y decidís comprar helado para tus hermanos, los cuales son amantes de la menta granizada y del dulce de leche con nuez. El negocio ofrece helado en todo tipo de formato, desde mini-cucuruchos hasta potes de 1 kilo, y cada formato cuesta cierta cantidad de dinero. Decidís gastar exactamente todo el dinero que te queda luego de haber ido al supermercado, de forma tal que no sobre ni falte.

# Programar una función que recibe una lista con los precios de los distintos formatos en que se vende el helado, y además reciba la cantidad de dinero disponible para gastar. La función debe encontrar la manera de comprar cierto formato de helado sabor menta, y cierto formato sabor dulce de leche, de manera de gastar la totalidad del dinero disponible. En consecuencia, la cantidad de formatos seleccionados debe ser exactamente 2, está permitido seleccionar el mismo formato para ambos sabores de helado. La función debe devolver con return una lista de 2 elementos, los cuales serán los precios de los formatos de helado seleccionados. En caso de no existir una combinación que satisface los requisitos se debe devolver [-1, -1].

# Tips:

# Al usar un set o un diccionario como estructura de datos pueden mejorar la velocidad con la que el programa analiza si cierto elemento se encuentra dentro de los datos. La operación mi_set = set( mi_lista ) puede serles de utilidad para este propósito.
# Ejemplos:

# buscar_precios( [1, 2, 3, 4, 5] , 8) => [3, 5]

# buscar_precios( [7, 4, 2, 6, 7, 7] , 4) => [2, 2]

# buscar_precios( [4, 3, 7, 5] , 5) => [-1, -1]

# ★★★  Challenge: Modificar la función para que el resultado sea 1 sólo número: La cantidad de maneras diferentes de conseguir el objetivo (si dos formatos tienen el mismo precio, igualmente califican como formatos diferentes).

# Func recibe lista precios y cant dinero y devuelva una posibilidad comprar helado
def buscar_precios(lista_precios, plata):
	set_precios = set(lista_precios)
	posibilidades = set()
	# posibilidades = 0
	for valor1 in set_precios:
		if valor1 < plata:
			for valor2 in set_precios:
				if plata - valor1 - valor2 == 0:
					#return [valor1,valor2]
					# posibilidades+=1
					if valor1 not in posibilidades and valor2 not in posibilidades:
						print("Agregando: " + str(valor1) +" " +str(valor2))
						posibilidades.update([valor1,valor2])
	# return[-1,-1]
	return round(posibilidades
print(buscar_precios( [1, 2, 3, 4, 5] , 8))
print(buscar_precios( [7, 4, 2, 6, 7, 7] , 4))

print(buscar_precios( [4, 3, 7, 5] , 5))
# Idem func pero devuelve la cant de formas de comprar helado

