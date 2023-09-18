'''
Escribir un programa que permita ingresar tres números enteros y 
mostrar el mayor el menor y el valor que esta en medio.
'''

number_one = int(input('Ingrese un numero: '))
number_two = int(input('Ingrese un numero: '))
number_three = int(input('Ingrese un numero: '))
number_max = max(number_one, number_two, number_three)
number_min = min(number_one, number_two, number_three)
number_mid = number_one + number_two + number_three - number_max -number_min
print(f'El numero maximo es {number_max}')
print(f'El numero minimo es {number_min}')
print(f'El numero restante es {number_mid}')