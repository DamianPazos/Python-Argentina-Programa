'''
Escribir un programa que lea números enteros hasta que se ingrese un 0, 
y muestre el promedio de los números ingresados.
'''

counter = 0
sum = 0
while True:
    number = int(input('Ingrese un numero'))
    if number != 0:
        counter += 1
        sum = sum + number
    else:
        break
print(f'El promedio es {sum/counter}')