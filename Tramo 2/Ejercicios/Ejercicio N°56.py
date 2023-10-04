'''
Escribir un programa que permita Leer números que representan edades de un grupo de personas, 
finalizando la lectura cuando se ingrese el número 999. 
Imprimir cuántos son menores de 18 años, cuántos tienen 18 años o más y el promedio de edad de ambos grupos. 
Descartar valores que no representan una edad válida. 
(Se considera válido una edad entre 0 y 100)
'''

check = True
counter_underage = 0
average_underage = 0
counter_adult = 0
average_adult = 0
while check:
    age = int(input('Ingrese la edad: '))
    if age < 18 and age >= 0:
        counter_underage += 1
        average_underage = average_underage + age
    elif age >= 18 and age <= 100:
        counter_adult += 1
        average_adult = average_adult + age
    elif age == 999:
        check = False
print(f'Hay {counter_underage} menores de edad y {counter_adult} mayores de edad, con un promedio de {round(average_underage / counter_underage, 2)} y {round(average_adult / counter_adult, 2)} respectivamente')