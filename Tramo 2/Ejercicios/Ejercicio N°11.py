'''
Tres personas aportan diferente capital a una sociedad y desean saber el valor total aportado y qué porcentaje aportó cada una 
(indicando nombre y porcentaje).
Solicitar la carga por teclado del nombre de cada socio y su capital aportado, 
a partir de esto calcular e informar lo requerido previamente.
'''

name_1 = input("Ingrese su nombre: ")
percentage_1 = float(input("Ingrese el porcentaje de capital aportado:"))
name_2 = input("Ingrese su nombre: ")
percentage_2 = float(input("Ingrese el porcentaje de capital aportado:"))
name_3 = input("Ingrese su nombre: ")
percentage_3 = float(input("Ingrese el porcentaje de capital aportado:"))
all_money = int(input("Ingrese el total del capital: $"))
print(f"{name_1} aporto un total de ${all_money * (percentage_1 / 100)}")
print(f"{name_2} aporto un total de ${all_money * (percentage_2 / 100)}")
print(f"{name_3} aporto un total de ${all_money * (percentage_3 / 100)}")