'''
Escribir un programa que permita ingresar una edad (entre 1 y 120 años), 
un género ('F'para mujeres, 'M' para hombres) y un nombre. 
En caso de haber ingresado valores erróneos (edad fuera de rango o género inválido), 
informar tal situación indicando el nombre de la persona. 
Si los datos están bien ingresados el programa debe indicar, 
sabiendo que las mujeres se jubilan con 60 años o más y los hombres con 65 años o más, 
si la persona está en edad de jubilarse.
'''

age = int(input('Ingrese una edad: '))
genre = input('Ingrese el genero, siendo "M" para masculino y "F" para femenino: ')
name = input('Ingrese el nombre: ')
if (age < 1 or age > 120) and (genre != 'F' and genre != 'M'):
    print(f'{name} ingreso una edad y un genero erroneo')
elif age < 1 or age > 120:
    print(f'{name} ingreso una edad erronea')
elif genre != 'F' and genre != 'M':
    print(f'{name} ingreso una genero erroneo')
else:
    if (genre == 'F' and age >= 60) or (genre == 'M' and age >= 65):
        print('Esta con edad para jubilarse')
    else:
        print('No se encuentra en edad para jubilarse')