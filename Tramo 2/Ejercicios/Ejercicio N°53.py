'''
Escribir un programa que permita ingresar nombre y edad de un grupo de personas (para cada una, nombre y edad). 
La carga termina cuando en el nombre de la persona se ingresa un asterisco ('*'). 
Mostrar al final cómo se llama la persona más joven.
'''

check = True
person = {
    'name': None,
    'Age': None
}
while check:
    name = input('Ingrese el nombre: ')
    if name != '*':
        age = int(input('Ingrese la edad: '))
        if person['Age'] == None:
            person['name'] = name
            person['Age'] = age
        elif person['Age'] > age:
            person['name'] = name
            person['Age'] = age
    else:
        check = False
print(f'La persona mas joven se llama {person["name"]} y tiene {person["Age"]} años')