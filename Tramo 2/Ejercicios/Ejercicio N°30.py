'''
Escribir un programa que permita al usuario ingresar dos números enteros. 
La computadora debe indicar si el mayor es divisible por el menor.
'''

number_one = int(input('Ingrese un numero: '))
number_two = int(input('Ingrese un numero: '))
if number_one % number_two == 0:
    print(f'El {number_one} es divisible por {number_two}')
else:
    print(f'El {number_one} no es divisible por {number_two}')