'''
Escribir un programa que permita al usuario ingresar un número entero y 
luego muestre un mensaje indicando si el número es par o impar.
'''

number = int(input('Ingrese un numero entero: '))
if number % 2 == 0:
    print('El numero es par')
else:
    print('El numero es impar')