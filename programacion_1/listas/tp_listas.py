import random

# Ejercicio 1 - Crear una lista con las notas de 10 estudiantes.
notas = []

for i in range(10):
    random_nota = random.randint(1, 10)
    notas.append(random_nota)

for i in range(10):
    print(f"Estudiante #{i + 1} - Nota: {notas[i]}")

sum_notas = 0
promedio = 0

for nota in notas:
    sum_notas += nota
    promedio = sum_notas / len(notas)

print(f"\nEl promedio total es: {promedio}")

nota_alta = max(notas)
nota_baja = min(notas)

print(f"\nLa nota más alta es: {nota_alta} y la nota baja es: {nota_baja}")

# Ejercicio 2 - Pedir al usuario que cargue 5 productos en una lista.
productos = []

while len(productos) < 5:
    producto = input("Por favor ingresa cinco productos para cargar en nuestra lista: ")
    productos.append(producto)

print(sorted(productos))

producto_a_eliminar = input("Por favor elige que producto a eliminar: ")

productos.remove(producto_a_eliminar)

print(f"Listo el producto {producto_a_eliminar} fue eliminado de la lista: {productos}")

# Ejercico 3 - Generar una lista con 15 números enteros al azar entre 1 y 100
lista = []
lista_pares = []
lista_impares = []

for i in range(15):
    lista.append(random.randint(1, 100))

print(f"Lista completa: {lista}")

for i in lista:
    if i % 2 == 0:
        lista_pares.append(i)
    else:
        lista_impares.append(i)

print(f"Lista de numeros pares: {lista_pares}")
print(f"Lista de numeros impares: {lista_impares}")

total_pares = 0

for i in lista_pares:
    total_pares += 1

print(f"La lista de pares tiene en total: {total_pares}")

total_impares = 0

for i in lista_impares:
    total_impares += 1

# Correcion -  La actividad 3 tiene un error menor al mostrar el conteo de impares
# Modifico la variable dentro del print para mostrar los valores correctos
print(f"La lista de impares tiene en total: {total_impares}")

# Ejercicio 4 - Dada una lista con valores repetidos
datos = [1, 3, 5, 3, 7, 1, 9, 5, 3]

datos_sin_repetir = list(set(datos))

print(datos_sin_repetir)

# Ejercicio 5 - Crear una lista con los nombres de 8 estudiantes presentes en clase
estudiantes = [
    "Francisco",
    "Dolores",
    "Jorge",
    "Juan",
    "Roberto",
    "Agostina",
    "Mora",
    "Manuela",
]

while True:
    choice = input(
        "Quieres agregar un nuevo estudiante o eliminar uno existente? A/E/S\t".lower().strip()
    )

    while not choice.isalpha() or not choice:
        print("Por favor selecciona A para agregar o E para eliminar o S para salir")
        choice = (
            input(
                "Quieres agregar un nuevo estudiante, eliminar uno existente o salir del programa? A/E/S"
            )
            .lower()
            .strip()
        )

    if choice == "a":
        estudiante = input("Por favor ingresa el nombre del estudiante a agregar: ")
        estudiantes.append(estudiante)

    # Correcion - La actividad 5 presenta un bug en la lógica de eliminación de estudiantes
    # Saco el .remove fuera de la validación de si se encuentra el estudiante en estudiantes
    elif choice == "e":
        estudiante_a_eliminar = input(
            "Por favor ingresa el nombre del estudiante a eliminar "
        )

        while estudiante_a_eliminar not in estudiantes:
            print(f"El estudiante {estudiante_a_eliminar} no se encuentra en la lista")
            estudiante_a_eliminar = input(
                "Por favor ingresa el nombre del estudiante a eliminar "
            )

        estudiantes.remove(estudiante_a_eliminar)
        print(f"El estudiante {estudiante_a_eliminar} fue eliminado correctamente")

    elif choice == "s":
        print("Saliendo del programa...")
        break
    else:
        print("Opcion no valida, utiliza A, E o S por favor")


print("Lista actualizada: ")
for i in estudiantes:
    print(f"{i}")

# Ejercicio 6 - Dada una lista con 7 números, rotar todos los elementos una posición hacia la derecha
# No, lo sacas con pop al ultima y lo insertas adelante
# Correcion - La actividad 6 no muestra la lista final rotada

numeros = []

for i in range(7):
    random_number = random.randint(1, 10)
    numeros.append(random_number)


print(f"Lista Original: {numeros}")

ultimo = numeros.pop()

numeros.insert(0, ultimo)

print(f"Lista rotada: {numeros}")

# 7 - Crear una matriz (lista anidada) de 7x2 con
# las temperaturas mínimas y máximas de una semana

filas = 7
columnas = 2

matriz = [[0] * columnas for i in range(filas)]

for fila in matriz:
    fila[0] = float(input("Ingresa un minimo para la temperatura: "))
    fila[1] = float(input("Ingresa un maximo para la temperatura: "))

for fila in matriz:
    print(fila)

print("Calculando promedio de las minimas y el de las maximas: ")
promedio_minima = 0
promedio_maxima = 0

for fila in matriz:
    promedio_minima += fila[0] / len(matriz)
    promedio_maxima += fila[1] / len(matriz)

print(f"Promedio de mínimas: {promedio_minima}")
print(f"Promedio de máximas: {promedio_maxima}")

# Correcion - La actividad 7 no implementa la identificación del día con mayor amplitud térmica.
max_amplitud = 0
dia_mayor_amplitud = 0

for i in range(len(matriz)):
    # calculamos la maxima menos la minima
    amplitud = matriz[i][1] - matriz[i][0]

    # si la amplitud es mayor a cero y despues a seguir iterando
    if amplitud > max_amplitud:
        max_amplitud = amplitud
        dia_mayor_amplitud = i + 1

print(
    f"\nEl día con mayor amplitud térmica fue el Día {dia_mayor_amplitud} con {max_amplitud} grados."
)

# Ejercicio 8 - Crear una matriz con las notas de 5 estudiantes en 3 materias

notas = 5
materias = 3
matriz = [[0] * materias for i in range(notas)]

for i in range(notas):
    for j in range(materias):
        matriz[i][j] = random.randint(1, 10)

for i in matriz:
    print(i)

promedio_estudiante = 0

for i in range(len(matriz)):
    promedio_estudiante = sum(matriz[i]) / materias
    print(f"El promediod el estudiante {i + 1} es: {promedio_estudiante}")

for j in range(materias):
    suma_materia = 0
    for i in range(notas):
        # Correcion - La actividad 8 tiene un error en el cálculo del promedio por materia.
        suma_materia += matriz[i][j]

    promedio_materia = suma_materia / notas

    print(f"El promediod de la materia {j + 1} es: {promedio_materia}")

# Ejercicio 9 - Representar un tablero de Ta-Te-Ti como una lista de listas (3x3)
# Correcion -  La actividad 9 muestra un entendimiento fundamentalmente incorrecto del juego Ta-Te-T
# Cambiamos para que el usuario pueda elegir tipo batalla naval donde en que posicion hace su jugada
turno = "x"
matriz = [["-"] * 3 for i in range(3)]

for i in range(9):
    for fila in matriz:
        print(fila)

    print(f"Es el turno de {turno}")

    fila = int(input("Ingresa fila a jugar (0, 1, 2)"))
    columna = int(input("Ingresa fila a jugar (0, 1, 2)"))

    if matriz[fila][columna] == "-":
        matriz[fila][columna] = turno

        if turno == "x":
            turno = "o"
        else:
            turno = "x"
    else:
        print("Esa posición se encuentra ya ocupada")

print("Resultado final: ")
for i in matriz:
    print(i)

# Ejercico 10 - Una tienda registra las ventas de 4 productos durante 7 días,
# en una matriz de 4x7.

filas = 4
columnas = 7

matriz = [[0] * columnas for i in range(filas)]

for i in range(filas):
    for j in range(columnas):
        matriz[i][j] = random.randint(1, 10)

for i in matriz:
    print(i)

print("Total vendido por cada producto: ")
for i in range(filas):
    suma_producto = sum(matriz[i])
    print(f"Producto {i + 1}: {suma_producto}")

mayor_venta = 0
dia_ganador = 0

print("Calculando el dia con mas ventas: ")
for j in range(columnas):
    suma_dia = 0
    for i in range(filas):
        venta = matriz[i][j]
        suma_dia += venta

    print(f"Total del día {j+1}: {suma_dia}")

    if suma_dia > mayor_venta:
        mayor_venta = suma_dia
        dia_ganador = j + 1

print(f"El día con mayores ventas fue el {dia_ganador} con un total de {mayor_venta}")

max_ventas_producto = 0
producto_ganador = 0

print("Analizando el producto con más ventas:")
for i in range(filas):
    total_producto = sum(matriz[i])
    print(f"Total del Producto {i + 1}: {total_producto}")

    if total_producto > max_ventas_producto:
        max_ventas_producto = total_producto
        producto_ganador = i + 1

print(
    f"El producto más vendido fue el {producto_ganador} con un total de {max_ventas_producto}"
)

# Ejercicio 11 - Crear una lista con los nombres de 10 estudiantes

estudiantes = [
    "Jorge",
    "Dolores",
    "Francisco",
    "Agostina",
    "Roberto",
    "Maria",
    "Josefina",
    "Juan",
    "Mariano",
    "Mora",
]

# Correcion - La actividad 11 falla si el nombre no se encuentra
# Cambio la estructura del if statement si no se encuentra el nombre en la lista

nombre_a_buscar = input("Ingrese un nombre a buscar: ")

if nombre_a_buscar in estudiantes:
    posicion_estudiante = estudiantes.index(nombre_a_buscar)
    print("El nombre se encuentra en la lista")
    print(f"El estudiante {nombre_a_buscar} está en la posición {posicion_estudiante}")

else:
    print("El nombre no se encuentra en la lista")

# Ejercicio 12 - Pedir al usuario que ingrese 8 números enteros y almacenarlos en una lista.

lista = []

for i in range(8):
    # Correcion - La actividad 12 ordena números como cadenas de texto
    numeros_a_ingresar = int(input("Por favor ingresa un numero para agregare a la lista: "))
    lista.append(numeros_a_ingresar)

print("Mostrando lista original: ")
for i in range(len(lista)):
    print(lista[i])

print("Mostrando la lista ordenada de menor a mayor: ")
lista_ordenada_menor = sorted(lista)

for i in range(len(lista_ordenada_menor)):
    print(lista_ordenada_menor[i])

print("Mostrando la lista ordenada de mayor a menor: ")
lista_ordenada_mayor = sorted(lista, reverse=True)

for i in range(len(lista_ordenada_mayor)):
    print(lista_ordenada_mayor[i])

# Ejercicio 13 - Dada la siguiente lista de puntajes de un videojuego

puntajes = [450, 1200, 875, 990, 300, 1500, 640]

# Correcion -  La actividad 13 no implementa el ranking y tiene un error
# en la búsqueda de posición
puntaje_mas_alto = max(puntajes)
puntaje_mas_bajo = min(puntajes)

print(f"El puntaje más alto es: {puntaje_mas_alto}")
print(f"El puntaje más bajo es: {puntaje_mas_bajo}")

objetivo_a_encontrar = 990

if objetivo_a_encontrar in puntajes:
    posicion = puntajes.index(objetivo_a_encontrar) + 1
    print(f"El puntaje {objetivo_a_encontrar} se encuentra en la posición: {posicion}")

ranking = sorted(puntajes, reverse=True)

for i in range(len(ranking)):
    print(f"{i + 1}° Puesto: {ranking[i]}")
