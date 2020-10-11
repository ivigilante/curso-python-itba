import importlib
import creador_funciones
import funciones_matematicas

# creador_funciones.agregar_funcion()
creador_funciones.test_func()
importlib.reload(funciones_matematicas)
print("Llamando a test")
funciones_matematicas.f()
# import funciones_matematicas

# def integral(f, a, b, dx):
# 	a1 = a
# 	b1 = a + dx
# 	area = 0
# 	while(b1 < b):
# 		area += f(a1) * dx
# 		a1 += dx
# 		b1 += dx
# 	return area

# a = 1
# b = 8
# dx = 0.00001
# print(integral(funciones_matematicas.f,a,b,dx))