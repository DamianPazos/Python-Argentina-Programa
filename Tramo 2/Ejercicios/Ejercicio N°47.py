'''
Escribir un programa que permita validar la nota de un examen. 
Se espera que la nota que el usuario ingrese sea un número comprendido entre 0 y 10.
La misma debe ser ingresada tantas veces como sea necesario hasta que quede comprendida dentro del rango indicado.
'''

while True:
    note = int(input('Ingrese la nota del examen: '))
    if note >= 0 and note <= 10:
        break
print(note)