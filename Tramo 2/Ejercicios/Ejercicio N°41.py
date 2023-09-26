'''
Escribir un programa que lea números enteros hasta que se ingrese un 0, y muestre el máximo.
'''
max_number = None
while True:
    number = int(input('Ingrese un numero: '))
    if max_number is None and number != 0:
        max_number = number
    elif number == 0:
        break
    else:
        if max_number < number:
            max_number = number
print(f'El maximo ingresado es {max_number}')