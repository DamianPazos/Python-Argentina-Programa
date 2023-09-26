'''
Escribir un programa que permita ingresar dos numeros enteros a y b. El programa debe mostrar:
La suma de los numeros pares entre a y b.
El producto de los numeros impares entre a y b.
'''

number_one = int(input('Ingresa un numero entero: '))
number_two = int(input('Ingresa otro numero entero: '))
sum = 0
product = 1
for x in range(number_one,number_two + 1):
    if x % 2 == 0:
        sum = sum + x
    else:
        product = product * x
print(f'La suma de los numeros pares es {sum}')        
print(f'El producto de los numeros impares es {product}')