'''
Una remisería requiere un sistema que calcule el precio de un viaje a partir de la cantidad de km que desea recorrer el usuario.
Tiene la siguiente tarifa:
Viaje mínimo $50
Si recorre entre 0 y 10km: $20/km
Si recorre 10km o más: $15/km
Escribir un programa que permita ingresar la cantidad de km que desea recorrer el usuario y muestre el precio del viaje.
'''

distance = int(input('Ingrese la cantidad de km a recorrer: '))
cost_trip = 50
if distance >= 10:
    cost_trip = cost_trip + distance * 15
    print(f'El costo del viaje es  ${cost_trip}')
else:
    cost_trip = cost_trip + distance * 20
    print(f'El costo del viaje es  ${cost_trip}')