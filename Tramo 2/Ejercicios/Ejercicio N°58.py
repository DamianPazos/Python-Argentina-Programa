'''
Una empresa aplica el siguiente procedimiento en la comercialización de sus productos:
Aplica el precio base a la primera docena de unidades.
Aplica un 10% de descuento a todas las unidades entre 13 y 100.
Aplica un 25% de descuento a todas las unidades por encima de las 100.
Escribir un programa que lea la cantidad solicitada de un producto y su precio base, 
y muestre el valor total de la venta y el precio promedio por unidad.
El fin de carga se determina ingresando -1 como cantidad solicitada.
Al finalizar informar:
a- Cantidad de ventas realizadas total.
b- Cantidad de ventas que se aplicaron un 10% de descuento.
c- Cantidad de ventas que SOLO se aplicó el precio base, no se le realizaron descuentos
'''

check = True
list_product = []
counter_all_sales = 0
counter_discount_sales = 0
counter_base_price_sales = 0
while check:
    product = {
        'price' : None,
        'quantity' : None
    }
    quantity = int(input('Ingrese la canitdad de unidades del producto: '))
    if quantity != -1 and quantity > 0:
        price = round(float(input('Ingrese el precio base del producto: $')), 2)
        if quantity > 12 and quantity <= 100:
            price = price - price * 0.1
            counter_discount_sales += 1
            counter_all_sales += 1
        elif quantity > 100:
            price = price - price * 0.25
            counter_all_sales += 1
        else:
            counter_all_sales += 1
            counter_base_price_sales += 1
        product['quantity'] = quantity
        product['price'] = price
        list_product.append(product)
        print(f'El precio total es ${product["price"] * product["quantity"]} y su precio por unidad es {product["price"]}')
    else:
        check = False
print(f'Cantidad de ventas: {counter_all_sales}')
print(f'Cantidad de ventas con 10% de descuento: {counter_discount_sales}')
print(f'Cantidad de ventas sin descuento: {counter_base_price_sales}')