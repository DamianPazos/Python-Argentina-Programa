'''
Escribir un programa que permita ingresar valores del mismo tipo para las variables num1 y num2. 
Una vez cargadas, mostrar ambas variables por pantalla, 
intercambiá sus valores (que lo cargado en num1 quede en num2, y viceversa) y volvé a mostrarlas actualizadas.
'''

number_1 = int(input("Ingresa un numero:"))
number_2 = int(input("Ingresa un numero:"))
print(f"El primer numero es {number_1} y el segundo es {number_2}")
number_aux = number_1
number_1 = number_2
number_2 = number_aux
print(f"Se intercambiaron los valores, ahora el primer numero es {number_1} y el segundo es {number_2}")