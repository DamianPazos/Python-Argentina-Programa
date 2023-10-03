'''
Escribir un programa que permita un programa que permita ingresar la estatura (en metros con decimales) 
de cada jugador de un equipo de básquet La carga finalizará al ingresar cero. 
Calcular y mostrar la estatura promedio del equipo.
'''

check = True
average_height = 0
counter = 0
while check:
    height = float(input('Ingrese la altura: '))
    if height != 0:
        counter += 1
        average_height = average_height + height
    else:
        check = False
print(f'La altura promedio es de {round(average_height / counter, 2)}')