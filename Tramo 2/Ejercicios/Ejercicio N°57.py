'''
Escribir un programa que permita ingresar los números de legajo de los alumnos de un curso y su nota de examen final. 
El fin de la carga se determina ingresando un -1 en el legajo.
Informar para cada alumno si aprobó o no el examen considerando que se aprueba con nota mayor o igual a 4. 
Se debe validar que la nota ingresada sea entre 1 y 10. Terminada la carga de datos, informar:
Cantidad de alumnos que aprobaron (nota >= 4). Cantidad de alumnos que desaprobaron el examen (nota < 4). 
Porcentaje de alumnos que están aplazados (nota == 1).
'''

list_students = []
counter_approved = 0
counter_unapproved = 0
counter_deferred = 0
check = True
while check:
    student = {
        'file' : None,
        'note_test' : None
    }
    file = int(input('Ingrese el legajo: '))
    if file != -1:
        note_test = float(input('Ingrese la nota del examen final:'))
        if note_test <= 10 and note_test >= 0:
            student['file'] = file
            student['note_test'] = round(note_test, 2)
            list_students.append(student)
    elif file == -1:
        check = False
for x in list_students:
    if x['note_test'] >= 4:
        counter_approved += 1
        print(f'El alumno con el legajo {x["file"]} aprobo el examen')
    else:
        if x['note_test'] == 1:
            counter_deferred += 1
        else:
            counter_unapproved += 1
        print(f'El alumno con el legajo {x["file"]} desaprobo el examen')
print(f'La cantidad de alumnos de aprobados es {counter_approved} y la cantidad de desaprobados es {counter_unapproved}')
print(f'El porcentaje de aplazados es {round((counter_deferred * 100) / (counter_deferred + counter_approved + counter_unapproved), 2)}%')