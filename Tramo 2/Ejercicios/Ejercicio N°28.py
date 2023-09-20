'''
Crear un programa que pida un número de mes (ejemplo 4) y escriba el nombre del mes en letras ("abril"). 
Verificar que el mes sea válido e informar en caso que no lo sea.
'''
MONTH = ('Enero', 'Febrero', 'Marzo', 'Abril', 'Mayo', 'Junio', 'Julio', 'Agosto', 'Septiembre', 'Octubre', 'Noviembre', 'Diciembre')
month_number = int(input('Ingrese el número de mes: '))
if month_number <= 12 and month_number >= 1:
    print(MONTH[month_number - 1])
else:
    print('El numero no es un mes valido')