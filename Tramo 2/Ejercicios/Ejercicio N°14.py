'''
Escribir un programa que permita al usuario ingresar el ancho y largo de un terreno en metros, 
junto con el valor del metro cuadrado de tierra. El programa debe calcular y mostrar el valor total del terreno. 
Además, debe calcular la cantidad de metros de alambre necesarios para cercar completamente el terreno a tres alturas distintas.
'''

width = float(input("Ingrese el ancho del terreno en metros: "))
long = float(input("Ingrese el largo del terreno en metros: "))
square_metre_value = float(input("Ingrese el valor por metro cuadrado: $"))
land_value = (width * long) * square_metre_value
metres_wire = (width * 2 + long * 2) * 3
print(f"El valor del terreno es de ${land_value} y la canitidad de metros de alambre necesarios para poderlo cercar es de {metres_wire} m")