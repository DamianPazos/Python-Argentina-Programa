'''
Escribir un programa que lea números enteros hasta que se la suma de éstos sea mayor que 100, 
y muestre la cantidad de números ingresados.
'''

counter = 0
sum = 0
while sum <= 100:
    number = float(input('Ingrese un numero: '))
    sum = sum + number
    counter += 1
print(f'La suma es de {sum}')
print(f'Se ingreso {counter} numeros')