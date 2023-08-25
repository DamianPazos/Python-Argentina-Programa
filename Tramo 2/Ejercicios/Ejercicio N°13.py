'''
Escribir un programa para calcular el importe a cobrar por un vendedor, 
considerando su sueldo fijo de $200000 pesos más el 16% del monto total de ventas realizadas durante un mes.
'''

SALARY_FIXED = 200000 # La variable esta en Mayuscula porque es una constante
total_sales = float(input("Ingrese el valor total de las ventas realizadas en el mes: $"))
print(f"Su sueldo es de ${SALARY_FIXED + total_sales * 0.16}")