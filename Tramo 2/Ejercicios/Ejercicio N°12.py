'''
Escribir un programa en Python que solicite al usuario ingresar dos valores que representen las medidas en grados de dos ángulos interiores de un triángulo. 
Luego, calcular y mostrar por pantalla el valor en grados del ángulo restante.
'''

value_1 = float(input("Ingrese los grados de uno de los angulos interiores de un triangulo: "))
value_2 = float(input("Ingrese los grados del otro angulo: "))
print(f"El angulo restante es de {180 - value_1 - value_2}°")