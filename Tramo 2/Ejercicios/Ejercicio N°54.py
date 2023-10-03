'''
Escribir un programa que permita controlar con validación el ingreso a un sitio web. 
Teniendo dos constantes con un nombre de usuario ("admin") y una contraseña ("123456"), 
el programa debe permitir al usuario ingresar sus credenciales. 
Si las mismas son erróneas, se volverán a pedir hasta un máximo de 3 intentos. Finalmente, 
la computadora debe mostrar alguno de los siguientes mensajes según sea el caso: "Acceso concedido" o 
"Se ha bloqueado la cuenta"
'''

USER = {
    'password' : '123456',
    'username' : 'admin'
}
check = True
counter = 0
while check:
    username = input('Ingrese su usuario: ')
    password = input('Ingrese su contraseña: ')
    if username == USER['username'] and password == USER['password']:
        print('Acceso concedido')
        check = False
    elif counter == 3:
        print('Se ha bloqueado la cuenta')
        check = False
    else:
        print('Se ha ingresado el usuario o la contraseña incorrecta')
        counter += 1