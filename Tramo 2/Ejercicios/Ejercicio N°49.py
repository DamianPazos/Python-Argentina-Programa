'''
Escribir un programa que permita validar una opción ingresada. 
Se le preguntará al usuario si desea continuar con alguna operación de la forma "¿Deseás continuar? [S/N]". 
Se espera que el usuario ingrese una 'S' o una 'N' (incluir las minúsculas). 
La opción debe ser ingresada tanto como sea necesario hasta que quede comprendida dentro de las posibilidades esperadas.
'''

check = True
while check:
    option = input('¿Deseás continuar? [S/N]: ')
    if option != 'S' and option != 's' and option != 'N' and option != 'n':
        pass
    else:
        check = False