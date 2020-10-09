def pintar_linea(values, first_black = False):
	linea = ""
	for val in values:
		for i in range(val):
			if first_black:
				linea += "##"
			else:
				linea += "  "
		first_black = not(first_black)
	print(linea)
pintar_linea([4,4,9,1])
pintar_linea([3,1,4,1,7,1,1,1])
pintar_linea([2,1,6,1,6,1,2,1])
pintar_linea([2,1,6,1,6,1,2,1])
pintar_linea([1,1,8,1,4,1,4,1])
pintar_linea([1,5,1,3,1,4,1,4,1], True)
pintar_linea([1,4,2,4,1,3,1,4,1], True)
pintar_linea([1,4,2,4,1,4,1,2,1,1], True)
pintar_linea([1,1,10,1,3,1,1,1])
pintar_linea([2,2,9,1,1,1,2,1])
pintar_linea([4,3,2,1,3,2,2,1])
pintar_linea([5,1,2,1,5,1,2,1])
pintar_linea([5,1,3,2,3,1,1,1])
pintar_linea([4,1,1,1,7,2])
pintar_linea([5,3,5,2])
pintar_linea([8,3,1,2])
pintar_linea([9,1,3,1])
pintar_linea([10,3])
# pintar_linea([])
# pintar_linea([])
# pintar_linea([])
# pintar_linea([])