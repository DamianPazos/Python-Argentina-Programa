'''
Escribir un programa que permita ingresar tres números enteros e indicar cual es el mayor.
'''

number_one = int(input('Ingrese un numero: '))
number_two = int(input('Ingrese un numero: '))
number_three = int(input('Ingrese un numero: '))
if (number_one >= number_two and number_one >= number_three):
    print(f'El mayor es {number_one}')
if (number_two > number_one and number_two >= number_three):
    print(f'El mayor es {number_two}')
if (number_three > number_one and number_two < number_three):
    print(f'El mayor es {number_three}')