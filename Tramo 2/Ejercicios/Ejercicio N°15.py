'''
Una inmobiliaria paga a sus vendedores un salario base, 
más una comisión fija por cada venta realizada, más el 5% del valor de esas ventas. 
Realizar un programa que imprima el nombre del vendedor y el salario que le corresponde en un determinado mes.
Se leen por teclado el nombre del vendedor, la cantidad de ventas que realizó y el valor total de las mismas.
'''

name = input("Ingrese su nombre: ")
sales_quantity = int(input("Ingrese la cantidad de ventas "))
sales_value = float(input("Ingrese el monto total de las ventas: $"))
SALARY_FIXED = 200000
COMMISSION = 50
total_salary = SALARY_FIXED + COMMISSION * sales_quantity + sales_value * 0.05
print(f"{name}, su sueldo es de ${total_salary}") 
