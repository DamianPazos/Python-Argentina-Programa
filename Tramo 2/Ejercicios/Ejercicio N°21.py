'''
Escribir un programa que permita ingresar dos números enteros e 
indicar si el primero es mayor, menor o igual al segundo.
'''

number_one = int(input('Ingrese un número entero: '))
number_two = int(input('Ingrese otro número entero: '))
if number_one > number_two:
    print('El primer numero es mayor que el segundo número')
if number_one == number_two:
    print('El primer número es igual al segundo número')
if number_one < number_two:
    print('El primer número es menor que el segundo número')