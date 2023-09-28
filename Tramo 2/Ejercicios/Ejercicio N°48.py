'''
Escribir un programa que permita realizar varias operaciones matemáticas ingresando un caracter 
por cada una la operación a realizar (‘+’, ‘-’, ‘*’, ‘/’, ‘F’) y dos números enteros en el caso que no haya elegido ‘F’. 
La computadora debe mostrar el resultado para la operación ingresada. 
Considerar que no se puede dividir por cero. 
Cuando la operación ingresada sea ‘F’ nos indicará que no se desean calcular más operaciones.
'''

check = True
while check:
    print('Las posibles operaciones son: \n"+" Suma\n"-" Resta\n"*" Multiplicacion\n"/" Division\n"F" Salir')
    operation = input('Ingrese la operacion que desea realizar: ')
    if operation != "+" and operation != '-' and operation != '*' and operation != '/'  and operation != 'F':
        print('Ingreso una opcion invalida')
    elif  operation == 'F':
        check = False
    else:    
        number_one = float(input('Ingrese el primer numero: '))
        number_two = float(input('Ingrese el segundo numero: '))
        if operation == '+':
            print(f'La suma es {number_one + number_two}')
        elif operation == '-':
            print(f'La resta es {number_one - number_two}')
        elif operation == '*':
            print(f'La multiplicacion es {number_one * number_two}')
        elif operation == '/' and number_two != 0:
            print(f'La suma es {number_one / number_two}')
        elif operation == '/' and number_two == 0:
            print('El divisor no puede ser 0 (cero)')