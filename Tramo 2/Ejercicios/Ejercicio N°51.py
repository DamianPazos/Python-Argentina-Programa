'''
Escribir un programa que permita al usuario ingresar números hasta que se introduzca un 0.
La computadora debe mostrar el número máximo y el número mínimo.
'''

check = True
max_number = None
min_number = None
while check:
    number = float(input('Ingrese un numero (Ingrese 0 para terminar): '))
    if max_number == None:
        max_number = number
    if min_number == None:
        min_number = number
    if max_number < number:
        max_number = number
    elif min_number > number:
        min_number = number
    elif number == 0:
        check = False
print(f'El numero maximo es {max_number} y el numero minimo es {min_number}')    