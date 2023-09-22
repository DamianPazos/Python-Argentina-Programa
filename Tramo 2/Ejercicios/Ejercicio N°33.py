'''
La farmacia Sindical efectúa descuentos a sus afiliados según el importe de la compra con la siguiente escala:
Menor de $5500.0 el descuento es del 4.5%
Entre $5500.0 y $10000.0 el descuento es del 8%
Más de $10000.0 el descuento es del 10.5%
Escribir un programa que reciba un importe e informe: el descuento y el precio neto a cobrar, con mensajes aclaratorios.
'''

cost_purchase = float(input('Ingrese el costo de la compra: $'))
if cost_purchase < 5500:
    cost_purchase = (cost_purchase * 95.5) / 100
    print(f'El costo es de ${cost_purchase} y tiene un descuento del 4.5%')
elif cost_purchase < 10000:
    cost_purchase = (cost_purchase * 92) / 100 
    print(f'El costo es de ${cost_purchase} y tiene un descuento del 8%')
else:
    cost_purchase = (cost_purchase * 89.5) / 100
    print(f'El costo es de ${cost_purchase} y tiene un descuento del 10.5%')