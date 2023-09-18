'''
Para acceder a cierta atracción, es necesario cumplir con dos requisitos: 
tener al menos 10 años de edad y medir más de 1,60 metros.

Escribir un programa en Python que solicite al usuario su edad y estatura, 
y que determine si cumple con los requisitos para subir a la atracción. 
Si cumple con ambos requisitos, el programa debe imprimir "¡Puede acceder!" en la pantalla. 
Si no cumple con alguno de los requisitos, el programa debe imprimir un mensaje que indique el motivo por el cual no puede subir. 
Por ejemplo, si no cumple con el requisito de la edad, el programa debe imprimir "Lo siento, eres demasiado joven para acceder." 
Si no cumple con el requisito de la estatura, el programa debe imprimir "Lo siento, eres demasiado bajo para acceder"
'''

age = int(input('Por favor, ingrese la edad: '))
height = float(input('Por favor ingrese la altura: '))
if age >= 10 and height > 1.60:
    print('¡Puede acceder!')
else:
    if height <= 1.60 and age < 10:
        print('No cumplis con ninguno de los dos requisitos')
    if height <= 1.60 and age >= 10:
        print('No cumplis el requisito de altura')
    if height > 1.60 and age < 10:
        print('No cumplis con el requisito de la edad')