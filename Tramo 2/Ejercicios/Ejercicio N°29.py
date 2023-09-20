'''
Escribir un programa que permita Ingresar las notas de los dos parciales de un alumno e indicar si promocionó, 
aprobó o debe recuperar. Si el valor de la nota no esta entre 0 y 10, debe informar un error.

Se promociona cuando las notas de ambos parciales son mayores o iguales a 7.
Se aprueba cuando las notas de ambos parciales son mayores o iguales a 4.
Se debe recuperar cuando al menos una de las dos notas es menor a 4.
'''

note_one = int(input('Ingrese la primer nota: '))
if note_one >= 0 and note_one <= 10:
    note_two = int(input('Ingrese la segunda nota: '))
    if note_two >= 0 and note_two <= 10:
        if note_one >= 7 and note_two >= 7:
            print('Promocionas la materia')
        elif note_one >= 4 and note_two >= 4:
            print('Apruebas la materia')
        else:
            print('Desapruebas la materia')
    else:
        print('Ingreso una nota erronea')    
else:
    print('Ingreso una nota erronea') 