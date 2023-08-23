'''
Escribir un programa para resolver el siguiente problema:
Tres personas invierten dinero para fundar una empresa (no necesariamente en partes iguales). 
Calcular qué porcentaje invirtió cada una.
'''

money_spent_1 = float(input("Ingrese el dinero a invertir: $"))
money_spent_2 = float(input("Ingrese el dinero a invertir: $"))
money_spent_3 = float(input("Ingrese el dinero a invertir: $"))
all_money_spent = money_spent_1 + money_spent_2 + money_spent_3
print(f"La primer persona invirtio un {round((money_spent_1*100)/all_money_spent, 2)}%, la segunda persona invirtio un {round((money_spent_2*100)/all_money_spent, 2)}% y la ultima persona invirtio {round((money_spent_3*100)/all_money_spent, 2)}%")