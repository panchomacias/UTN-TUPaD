nombre_cliente = input("Ingresa tu nombre: ")
while not nombre_cliente.isalpha():
    print("Por favor ingresa solo letras")
    nombre_cliente = input("Ingresa tu nombre: ")

cantidad_productos = input("Ingresa la cantidad de productos a comprar: ")
while not cantidad_productos.isdigit():
    print("Por favor ingresa un numero entero")
    cantidad_productos = input("Ingresa la cantidad de productos a comprar: ")

cantidad_productos = int(cantidad_productos)

total_sin_descuento = 0
total_con_descuento = 0

for i in range(1, cantidad_productos + 1):
    precio = input("Por favor ingresa un precio: ")
    while not precio.isdigit():
        print("Por favor ingresa un numero entero")
        precio = input("Por favor ingresa un precio: ")

    precio = int(precio)

    total_sin_descuento += precio

    descuento = input("Tiene descuento? Elegir: S / N ").upper()
    while not descuento.isalpha():
        print("Por favor ingresa S o N")
        descuento = input("Tiene descuento? Elegir: S / N ").upper()

    if descuento == "S":
        precio_final = precio * 0.90
    else:
        precio_final = precio

    total_con_descuento += precio_final

    print(f"Cliente: {nombre_cliente}")
    print(f"Producto {i} - Precio: {int(precio_final)} - Descuento (S/N): {descuento}")

ahorro = total_sin_descuento - total_con_descuento
promedio = total_con_descuento / cantidad_productos

print(f"Total sin descuento: ${total_sin_descuento} ")
print(f"Total con descuento: ${total_con_descuento}")
print(f"Ahorro: ${ahorro}")
print(f"Promedio por producto: {promedio}")
