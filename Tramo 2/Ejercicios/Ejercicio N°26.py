'''
Escribir un programa que permita ingresar la cantidad de invitados a una fiesta y la cantidad de asientos disponibles en el salon. 
Debes indicar si alcanzan los asientos, Si los asientos no alcanzaran indicar cuántos faltan para que todos los invitados puedan sentarse.
'''

guests = int(input('Ingrese la cantidad de invitados: '))
chairs_available = (int(input('Ingrese la cantidad de asientos disponibles: ')))
if guests <= chairs_available:
    print('La capacidad del salon alcanza para la cantidad de invitados')
else:
    print(f'Faltan {guests - chairs_available} sillas para los invitados ')