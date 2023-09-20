'''
Una editorial determina el precio de un libro según la cantidad de páginas que contiene. 
El costo básico del libro es de $1000, más $35,10 por página con encuadernación rústica. 
Si el número de páginas supera las 300 la encuadernación debe ser especial, lo que incrementa el costo en $1200. 
Además, si el número de páginas sobrepasa las 600 se hace necesario otro procedimiento de encuadernación que incrementa el costo en $880. 
Desarrollar un programa que calcule el costo de un libro dado el número de páginas.
'''

number_pages = int(input('Inserte la cantidad de paginas del libro: '))
PAGE_PRICE = 35.10
book_price = 1000 + PAGE_PRICE * number_pages 
if number_pages > 300:
    book_price += 1200
    if number_pages > 600:
        book_price += 800
print(f'El costo del libro es ${book_price}')