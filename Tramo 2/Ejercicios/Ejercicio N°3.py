'''
Escribir un programa que solicite al usuario su nombre y su edad, 
despues pida una cantidad de años y muestre por pantalla un mensaje que indique cuantos años tendra la persona después de sumarle a su edad la cantidad de años ingresada.
El mensaje debe tener el siguiente formato:
"Hola, [nombre].Dentro de [cantidad] años tendras [edad + cantidad] años.".
'''

name = input("Ingrese su nombre: ")
age = int(input("Ingrese su edad: "))
number = int(input("Ingrese una cantidad de años a sumar: "))
print(f"Hola, {name}.Dentro de {number} años tendras {age + number} años.")