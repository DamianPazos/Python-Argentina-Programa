'''
Un entrenador le ha propuesto a un atleta recorrer una ruta de cinco kilómetros durante 10 días para determinar 
si es apto para la prueba de 5 kilómetros que se desarrollará en el Parque. 
No se sabe si está apto y para eso nos piden que hagamos el siguiente programa.
Nos ingresan por cada día de entrenamiento tiempo de la prueba en minutos (entero mayor que 0 y menor a 100)
Para considerarlo apto debe cumplir las siguientes condiciones:
Que en ninguna de las pruebas haga un tiempo mayor a 20 minutos.
Que al menos en una de las pruebas realice un tiempo menor de 15 minutos.
Que su promedio sea menor o igual a 18 minutos.
Se pide:
Diseñar un algoritmo para registrar los datos y decidir si es apto para la competencia. 
*Sólo en caso de estar apto, informar el promedio y el número de día en el que realizó el menor tiempo
'''

def control_time(quantity):
    list_time = []
    for x in range(quantity):
        time = int(input('Ingrese el tiempo: '))
        list_time.append(time)
    return list_time
def average(list):
    sum_time = 0
    for x in list:
        sum_time = sum_time + x
    return sum_time / len(list)
def min_time(list):
    time = None
    for x in list:
        if time == None:
            time = x
        elif time > x:
            time = x
    return time
def apt(list):
    flag = False
    for x in list:
        if x > 20:
            return False
        elif x < 15:
            flag = True
    if flag == True and average(list) <= 18:
        return True
    else: 
        return False
list_time_athlete = control_time(10)
is_apt = apt(list_time_athlete)
if is_apt == True:
    print('Es apto')
    print(f'Menor tiempo {min_time(list_time_athlete)} minutos')
    print(f'Tiempo promedio {average(list_time_athlete)}')
else:
    print('No es apto')