'''
Escribir un programa que permita leer dos números A y B (enteros positivos). 
Calcular el producto A * B por sumas sucesivas e imprimir el resultado.
'''

number_one = int(input('Ingrese un numero (Entero positivo): '))
number_two = int(input('Ingrese otro numero (Entero positivo): '))
product = 0
if number_one > 0 or number_two > 0:
    for x in range(number_two):
        product = product + number_one
    print(f'El resultado es {product}')
else:
    print('Ingresaste un numero negativo o cero')