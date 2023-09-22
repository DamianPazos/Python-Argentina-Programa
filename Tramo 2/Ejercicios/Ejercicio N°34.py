'''
Escribir un programa que calcule y muestre el sueldo neto de un empleado en base a su sueldo básico y su antigüedad en años. 
Si es soltero se le incrementa el sueldo en 5% del salario bruto por cada año de antigüedad, 
mientras que si es casado se le incrementa el sueldo en 7% del salario bruto por cada año de antigüedad. 
También se le realizan los siguientes descuentos:
Jubilación: 11%
Obra Social: 3%
Sindicato: 3%
Como datos de entrada se ingresa por teclado el sueldo básico, antigüedad y estado civil (S: Soltero / C: Casado). 
Se debe informar: (reemplazando los 9 por los valores que correspondan)
Estado Civil: Soltero/Casado Sueldo básico: $ 999.99 Antigüedad: 99 años
Descuentos:
Jubilación - 999,99
Obra Social - 999,99
Sindicato - 999,99
Sueldo Neto 999,99
'''

basic_salary = float(input('Ingres el sueldo basico del empleado: $'))
seniority = int(input('Ingrese la cantidad de años de antiguedad: '))
marital_status = input('Ingrese el estado civil (S: Soltero / C: Casado): ')
net_salary = 0
if marital_status == 'S':
    marital_status = 'Soltero'
    net_salary =  (basic_salary + (seniority * 0.05 * basic_salary)) * 0.83 
elif marital_status == 'C':
    marital_status = 'Casado'
    net_salary =  (basic_salary + (seniority * 0.07 * basic_salary)) * 0.83
print(f'Estado civil: {marital_status}')
print(f'Sueldo basico: ${basic_salary}')
print(f'Antiguedad: {seniority} años')
print('Descuentoss')
print(f'Jubilacion: ${basic_salary * 0.11} ')
print(f'Obra Social: ${basic_salary * 0.03}')
print(f'Sindicato: ${basic_salary * 0.03}')
print(f'Sueldo neto: ${net_salary}')