'''
Escribir un programa que solicite al usuario ingresar tres numeros enteros.
El programa debe mostrar por pantalla el resultado de sumar los tres numeros de la siguiente manera:
"[numero1] + [numero2] + [numero3] = [suma]".
'''

number_1 = int(input("Ingrese un numero: "))
number_2 = int(input("Ingrese un numero: "))
number_3 = int(input("Ingrese un numero: "))
print(f"{number_1} + {number_2} + {number_3} = {number_3 + number_2 + number_1}")