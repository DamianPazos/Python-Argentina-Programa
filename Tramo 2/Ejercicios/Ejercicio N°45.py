'''
Escribir un programa que permita leer dos números naturales A y B. 
Calcular A elevado a la B mediante productos sucesivos y mostrar el resultado.
'''

number_one = int(input('Ingrese un numero: '))
number_two = int(input('Ingrese otro numero: '))
product = 1
for x in range(number_two):
    product = product * number_one
print(f'El resultado es {product}')