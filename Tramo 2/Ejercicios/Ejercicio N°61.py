'''
Escribir un programa que permita ingresar un número entero positivo y mostrar su factorial. 
El factorial de un número es el producto de todos los números enteros desde 1 hasta el número ingresado. 
'''

def factorial(nro):
    if nro == 0:
        return 1
    else:
        return factorial(nro - 1)* nro
number = int(input('Ingrese un numero entero positivo: '))
print(factorial(number))