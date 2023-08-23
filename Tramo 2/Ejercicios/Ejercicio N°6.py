'''
Escribir un programa que solicite al usuario ingresar tres notas de un alumno.
El programa debe mostrar por pantalla las notas separadas por comas en un reglon y el promedio de las notas en el siguiente reglon.
'''

score_1 = int(input("Ingrese el valor de la primer nota:" ))
score_2 = int(input("Ingrese el valor de la segunda nota: "))
score_3 = int(input("Ingrese el valor de la tercer nota:" ))
print(f"Notas: {score_1}, {score_2}")
print(f"Promedio: {(score_2 + score_1 + score_3)/3}")