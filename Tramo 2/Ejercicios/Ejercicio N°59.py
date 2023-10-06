'''
Escribir un programa para un negocio de venta de granos que desea controlar las ventas realizadas. 
De cada venta ingresa el importe total y un código que indica la forma de pago. Los códigos puede ser:
C: cheque, 20% de recargo.
E: efectivo, 10% de descuento.
T: con tarjeta, 12% de recargo.
Se debe ingresar una F para finalizar el día de venta y arrojar los siguientes totales.
| Forma de Pago    | Total     |
| ---------------- | --------- | 
| Efectivo en Caja | $ xxxx.xx |
| Tarjeta Crédito  | $ xxxx.xx |
| Cheques          | $ xxxx.xx |
| Total de Venta   | $ xxxx.xx |
| Importe del IVA  | $ xxxx.xx |
'''

cash = 0
check = 0
credit_card = 0
flag = True
while flag:
    amount_received = round(float(input('Ingrese el importe cobrado: $')), 2)
    payment_method = input('Ingrese el metodo de pago: ')
    if payment_method == 'C' or payment_method == 'c':
        amount_received = amount_received + amount_received * 0.2
        check = check + amount_received
    elif payment_method == 'E' or payment_method =='e':
        amount_received = amount_received - amount_received * 0.1
        cash = cash + amount_received
    elif payment_method == 'T' or payment_method == 't':
        amount_received = amount_received + amount_received * 0.12
        credit_card = credit_card + amount_received
    elif payment_method == 'F' or payment_method == 'f':
        flag = False
    else:
        print('Ingreso una opcion incorrecta, vuelva a ingresar los datos')
print('| Forma de Pago    | Total     ')
print('| ---------------- | --------- ')
print(f'| Efectivo en Caja | $ {cash} ')
print(f'| Tarjeta Crédito  | $ {credit_card} ')
print(f'| Cheques          | $ {check} ')
print(f'| Total de Venta   | $ {cash + credit_card + check} ')
print(f'| Importe del IVA  | $ {round((cash + credit_card + check) * 0.21, 2)} ')
