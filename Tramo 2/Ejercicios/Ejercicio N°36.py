'''
Escribir un programa que permita ingresar dos números enteros y la operación a realizar('+', '-', '*', '/'). 
Debe mostrarse el resultado para la operación ingresada. 
Considerar que no se puede dividir por cero (en ese caso mostrar el texto 'ERROR').
'''

number_one = float(input('Ingrese un número: '))
number_two = float(input('Ingrese un número: '))
operator = input('Ingrese un operador ("+", "-", "*", "/"): ')
if operator == '+':
    print(number_one + number_two)
elif operator == '-':
    print(number_one - number_two)
elif operator == '*':
    print(number_one * number_two)
elif operator == '/':
    if number_two == 0:
        print('ERROR')
    else:
        print(number_one / number_two)
else:
    print('Ingreso un operador incorrecto')