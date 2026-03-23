# 1 - Crear un programa que imprima por pantalla el mensaje: “Hola Mundo!”.

print("Hola Mundo!")

# 2 -  Crear un programa que pida al usuario su nombre e
# imprima por pantalla un saludo usando el nombre ingresado

name = input("Me podrias indicar cual es tu nombre? ")
print(f"Un gusto {name}!")

# 3 - Crear un programa que pida al usuario su nombre, apellido,
# edad y lugar de residencia e imprima por pantalla una oración con los datos ingresados.

nombre = input("Me podrias indicar cual es tu nombre? ")
apellido = input("Me podrias indicar cual es tu apellido? ")
edad = int(input("Me podrias indicar tu edad? "))
pais = input("Me podrias indicar el pais en el cual residis? ")

print(f"Soy {nombre} {apellido}, tengo {edad} años y vivo en {pais} ")

# 4 - Crear un programa que pida al usuario el radio de un círculo
# e imprima por pantalla su área y  su perímetro.

radio = float(input("Cual es el radio de un circulo? "))
print(f"El area del circulo es: {3.1416 * (radio)**2}")
print(f"El permitero del circulo es: {2 * 3.1416 * radio}")

# 5 - Crear un programa que pida al usuario una cantidad de segundos
# e imprima por pantalla a cuántas horas equivale.

segundos = int(input("Ingresa la cantidad de segundos: "))
print(f"Los {segundos} ingresados equivalen a {segundos / 3600} horas")

# 6 - Crear un programa que pida al usuario un número
# e imprima por pantalla la tabla de multiplicar de dicho número.

numero = int(input("Ingresa un numero: "))
print(f"Tabla de {numero}: ")
for i in range(1, 11):
    print(f"{numero} x {i} = {numero * i}")

# 7 - Crear un programa que pida al usuario dos números enteros distintos del 0
# y muestre por pantalla el resultado de sumarlos, dividirlos, multiplicarlos y restarlos.

num1 = int(input("Ingresa el primer numero: "))
num2 = int(input("Ingresa el segundo numero: "))
operator = input("Ingresa el operador: (+, -, *, /)")

match operator:
    case "+":
        print(f"Resultado: {num1 + num2}")
    case "-":
        print(f"Resultado: {num1 - num2}")
    case "*":
        print(f"Resultado: {num1 * num2}")
    case "/":
        print(f"Resultado: {num1 / num2}")

# 8 - Crear un programa que pida al usuario su altura y su peso e
# imprima por pantalla su índice de masa corporal.

altura = float(input("Ingresa tu altura: "))
peso = float(input("Ingresa tu peso: "))

imc = peso / (altura) ** 2

print(f"Tu indice de masa corporal es: {imc}")

# 9 - Crear un programa que pida al usuario una temperatura
# en grados Celsius e imprima por pantalla su equivalente en grados Fahrenheit.

celsius = float(input("Ingresa una temperatura en grados celsius: "))
fahrenheit = 9 / 5 * celsius + 32

print(f"El equivalente ingresado en fahrenheit es: {fahrenheit} ")

# 10 - Crear un programa que pida al usuario 3 números e
# imprima por pantalla el promedio de dichos números.

def prom(num1, num2, num3):
    return (num1 + num2 + num3) / 3

num1 = float(input("Ingresa el primer numero para calcular el promedio: "))
num2 = float(input("Ingresa el segundo numero para calcular el promedio: "))
num3 = float(input("Ingresa el tercer numero para calcular el promedio: "))

print(f"El promedio es: {prom(num1, num2, num3)} ")
