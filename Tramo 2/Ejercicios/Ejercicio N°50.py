'''
Escribir un programa que permita validar la nota de un examen. 
Se espera que la nota que el usuario ingrese sea un número comprendido entre 0 y 10.
La misma debe ser ingresada tantas veces como sea necesario hasta que quede comprendida dentro del rango indicado.
Las notas 1 y 3 no usan nunca.
La nota 0 se reserva para los ausentes.
Las notas válidas pueden ser un 2 o un valor entre 4 y 10.
'''

check = True
while check:
    note = float(input('Ingrese la nota del examen: '))
    if note <= 10 and note >= 0:
        if note == 0:
            print('Ingreso un ausente')
            check = False
        elif note == 1 or note == 3:
            print('Reingrese la nota ya que este valor no se putiliza')
        else:
            print(f'La nota es {note}')
            check = False
    else:
        print('Ingreso un valor invalido, intente nuevamente')