#  El ejercicio más integrador

# Se pide calcular una integral definida en un intervalo de una función genérica.
# En lugar de obtener un resultado exacto, realizaremos una aproximación 
# del resultado aplicando la integral de Riemann. 
# Para lograr esto vamos a aproximar una función mediante muchos rectángulos 
# muy angostos. Para obtener el resultado de la integral vamos a sumar el área de todos 
# estos rectángulos entre cierto intervalo  [𝑎,𝑏] :
# 
# Primero debemos elegir un número  Δ𝑥  cuyo valor sea muy pequeño, y que 
# determina el ancho de los rectángulos. Comenzando del límite de integración 
# inferior  𝑎  obtendremos el primer área como  𝑓(𝑎)⋅Δ𝑥 , luego el siguiente 
# área será  𝑓(𝑎+Δ𝑥)⋅Δ𝑥  , el tercer área es  𝑓(𝑎+2⋅Δ𝑥)⋅Δ𝑥  , y así se sigue 
# mientras no se supere  𝑏 .
#
# Al elegir un valor más chico de  Δ𝑥  se obtiene una mejor aproximación:
# Se debe programar la función integral(f, a, b, dx) en la cual f sea la 
# función a integrar (debe recibir como parámetro un número x, debe entregar el 
# resultado usando return), a y b sean los límites de integración, y 
# dx sea el ancho de los rectángulos.

def integral(f, a, b, dx):
	a1 = a
	b1 = a + dx
	area = 0
	while(b1 < b):
		area += f(a1) * dx
		a1 += dx
		b1 += dx
	return area