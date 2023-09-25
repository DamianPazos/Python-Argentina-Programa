'''
Escribir un programa que permita ingresar un número entero n. Debe mostrar los primeros 10 múltiplos de n.
'''

number = int(input('Ingrese un número: '))
counter = 0
while counter < 10:
    if number % 10 == 0:
        print(number)
        number += 1
        counter += 1
    else:
        number += 1