'''
Escribir un programa que a partir de un número entero cant ingresado por el usuario permita cargar por teclado cant números enteros. 
La computadora debe mostrar cuál fue el mayor número y en qué posición apareció.
'''

quantity_number = int(input('Ingrese la cantidad de números a cargar: '))
max_number = {
    'value': None,
    'position': None,
}
for x in range(quantity_number):
    number = float(input('Ingrese un numero: '))
    if x == 0:
        max_number['value'] = number
        max_number['position'] = x + 1
    else:
        if max_number['value'] < number:
            max_number['value'] = number
            max_number['position'] = x + 1
print(f'El valor mas alto fue {max_number["value"]} y su posicion fue {max_number["position"]}')