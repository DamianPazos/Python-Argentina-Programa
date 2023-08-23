'''
Escribir un programa que solicite al usuario ingresar dos notas de un alumno.
El programa debe mostrar por pantalla el promedio de las notas de la siguiente manera:
"Notas: [nota1], [nota2] ==> promedio: [(nota1+nota2)/2]
'''

score_1 = int(input("Ingrese el valor de la primer nota:" ))
score_2 = int(input("Ingrese el valor de la segunda nota: "))
print(f"Notas: {score_1}, {score_2} ==> promedio: {(score_2 + score_1)/2}")