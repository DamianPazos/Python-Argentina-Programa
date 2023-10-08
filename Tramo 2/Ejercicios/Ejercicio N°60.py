'''
Escribir un programa para calcular el sueldo final a pagar a cada empleado de una empresa. 
De cada uno se tiene, sueldo básico, antigüedad, cantidad de hijos y estudios superiores (‘S’ o ‘N’). 
Además, se conocen los porcentajes de aumento del sueldo que dependen de los siguientes factores:
Si el empleado tiene más de 10 años de antigüedad: aumento del 10%
Si el empleado tiene más de 2 hijos: aumento del 10%, si solo tiene uno 5%
Si el empleado posee estudios superiores: aumento del 5%
Luego de ingresar los datos de un empleado se debe preguntar si se desea ingresar otro empleado o no. 
Se termina la carga cuando no se deseen ingresar más empleados.
Determinar: 
a. Por cada empleado: número de empleado, el sueldo básico y el nuevo sueldo. 
b. Sueldo nuevo promedio de la empresa.
'''

list_employee = []
flag = True
average_salary = 0
while flag:
    employee = {
    'basic_salary' : None,
    'seniority' : None,
    'number_children' : None,
    'higher_education': None
    }
    employee['basic_salary'] = float(input('Ingrese el salario basico: $'))
    employee['seniority'] = int(input('Ingrese la antiguedad en años: '))
    employee['number_children'] = int(input('Ingrese la cantidad de hijos: '))
    employee['higher_education'] = input('Tiene estudios superiores S / N: ')
    while employee['higher_education'] != 'S' and employee['higher_education'] != 's' and employee['higher_education'] != 'n' and employee['higher_education'] != 'N': 
        print('Ingreso un valor erroneo')
        employee['higher_education'] = input('Tiene estudios superiores S / N: ')
    list_employee.append(employee)
    option = input('Desea ingresar un nuevo empleado (S/N): ')
    while option != 'S' and option != 's' and option != 'n' and option != 'N': 
        print('Ingreso un valor erroneo')
        option = input('Desea ingresar un nuevo empleado (S/N): ')
    if option == 'n' or option == 'N':
        flag = False
for i,x in enumerate(list_employee):
    new_salary = x['basic_salary']
    if x['seniority'] > 10:
        new_salary = new_salary + x['basic_salary'] * 0.1
    if x['number_children'] == 1:
        new_salary = new_salary + x['basic_salary'] * 0.05
    elif x['number_children'] >= 2:
        new_salary = new_salary + x['basic_salary'] * 0.1
    if x['higher_education'] == 'S' or x['higher_education'] == 's':
        new_salary = new_salary + x['basic_salary'] * 0.05
    print(f'Empleado N°{ i + 1}')
    print(f'Sueldo basico {x["basic_salary"]} y sueldo con los porcentajes de aumento {new_salary}')
    average_salary = average_salary + new_salary
print(f'El promedio de sueldo de la empresa es {average_salary / (len(list_employee))}')