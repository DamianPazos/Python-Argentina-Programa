'''
Existen dos reglas que identifican dos conjuntos de valores:
a) El número es de un solo dígito.
b) El número es impar.
A partir de estas reglas, escribir un programa que permita ingresar un número entero.
Debe asignar el valor que corresponda a las variables booleanas:
esDeUnSoloDigito
esImpar
estaEnAmbos
noEstaEnNinguno
el valor Verdadero o Falso, según corresponda, para indicar si el valor número ingresado pertenece o no a cada conjunto.
'''

number = int(input('Ingrese un numero: '))
esDeUnSoloDigito = False
esImpar = False
estaEnAmbos = False
noEstaEnNinguno = False
if number >= 0 and number <= 9:
    esDeUnSoloDigito = True
if number % 2 == 0:
    esImpar = True
if esDeUnSoloDigito and esImpar:
    estaEnAmbos = True
elif not estaEnAmbos and not esDeUnSoloDigito:
    noEstaEnNinguno = True
print(f'Es de un solo digito: {esDeUnSoloDigito}')
print(f'Es impar: {esImpar}')
print(f'Corresponde a las 2 reglas: {estaEnAmbos}')
print(f'No corresponde a ninguna de las 2 reglas: {noEstaEnNinguno}')