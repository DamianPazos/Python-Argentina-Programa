'''
Escribir un programa que permita ingresar el valor monetario de una hora de trabajo y la cantidad de horas trabajadas por día, 
para calcular el salario semanal de un trabajador que trabaja todos los días hábiles y la mitad de las horas del día hábil los sábados, 
suponiendo que todas las horas tienen el mismo valor."
Mostrar el resultado del salario semanal en la pantalla.
'''

time_value = float(input("Ingresa el valor de una hora de trabajo: $"))
time_work = int(input("Ingrese la cantidad de horas por dia realizadas: "))
week_days = 5 # Cantidad de dias habiles
daily_value = time_value * time_work
week_value = daily_value * week_days
time_work_saturday = time_work / 2
weekly_salary = week_value + (time_value * time_work_saturday)
print(f"El salario semana es de ${weekly_salary}")