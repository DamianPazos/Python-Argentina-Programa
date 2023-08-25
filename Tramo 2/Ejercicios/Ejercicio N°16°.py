'''
Escribir un programa que permita al usuario ingresar un período de tiempo en segundos. 
Luego, el programa debe convertir ese período de tiempo a una forma más legible y comprensible para el usuario, expresando el resultado en días, horas, minutos y segundos. 
El resultado se mostrará en pantalla en un mensaje que indique la cantidad de segundos ingresados y su equivalente en días, horas, minutos y segundos.
'''

time = int(input("Ingrese una cantidad de tiempo en segundos: "))
days = time // 86400 # 86400 segundos equivalen a un dia - "//" division sin resto
hours = (time % 86400) // 3600 # 3600 segundos equivalen a una hora - "%" calcula el resto de una division
minutes = (time % 3600) // 60 # 60 segundos equivalen a un minuto
seconds = time % 60
print(f"Ingreso la cantidad de {time} segundos, que equivalen a {days} dias, {hours} horas, {minutes} minutos y {seconds} segundos")
