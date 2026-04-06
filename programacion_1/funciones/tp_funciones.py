import math

# Ejercicio 1 - Crear una función llamada imprimir_hola_mundo que imprima por pantalla 
# el mensaje: “Hola Mundo!”. Llamar a esta función desde el programa principal.

def hola_mundo():
    print("Hola Mundo!")

hola_mundo()

# Ejercicio 2 - Crear una función llamada saludar_usuario(nombre) que reciba como 
# parámetro un nombre y devuelva un saludo personalizado.

def saludar_usuario(nombre):
    print(f"Hola {nombre}!")

saludar_usuario("Francisco")

# Ejercicio 3 - Crear una función llamada informacion_personal(nombre, apellido, edad, 
# residencia) que reciba cuatro parámetros e imprima: “Soy [nombre] [apellido], tengo [edad] años y vivo en [residencia]”

nombre = input("Cual es tu nombre? ")
apellido = input("Cual es tu apellido? ")
edad = input("Cual es tu edad? ")
residencia = input("Cual es tu residencia? ")

def informacion_personal(nombre, apellido, edad, residencia):
    print(f"Soy {nombre} {apellido}, tengo {edad} años y vivo en {residencia}")

informacion_personal(nombre, apellido, edad, residencia)

# Ejercicio 4 - Crear dos funciones: calcular_area_circulo(radio) que reciba el ra- dio como parámetro y devuelva el área del círculo. calcular_perimetro_circulo(radio) 
# que reciba el radio como parámetro y devuel- va el perímetro del círculo. 

def calcular_area_circulo(radio):
    area = math.pi * (radio ** 2)
    return area


def calcular_perimetro_circulo(radio):
    perimetro = 2 * math.pi * radio
    return perimetro

radio = float(input("Ingresa el radio para calcular el permitro y el area del circulo: "))

print(calcular_area_circulo(radio))
print(calcular_perimetro_circulo(radio))

# Ejercicio 5 - Crear una función llamada segundos_a_horas(segundos) que reciba una cantidad de segundos como parámetro y devuelva la cantidad 
# de horas correspondientes

def segundos_a_horas(segundos):
    horas = segundos / 3600
    return horas

segundos = int(input("Ingresa por favor los segundos: "))

print(segundos_a_horas(segundos))

# Ejercicio 6 - Crear una función llamada tabla_multiplicar(numero) 
# que reciba un número como parámetro y imprima la tabla de multiplicar de ese número del 1 al 10. 

def tabla_multiplicar(numero):
    for i in range(1, 11):
        resultado = numero * i
        print(f"{numero} x {i} = {resultado}")

numero = int(input("Ingrese un numero: "))

tabla_multiplicar(numero)

# Ejercicio 7 - Crear una función llamada operaciones_basicas(a, b) 
# que reciba dos números como parámetros y devuelva una tupla con el resulta- do de sumarlos, restarlos, multiplicarlos y dividirlos. Mostrar los re- sultados de forma clara.

def operaciones_basicas(a, b):
    return (a + b, a - b, a * b, a / b)

num_a = 10
num_b = 2

suma, resta, multiplicacion, division = operaciones_basicas(num_a, num_b)

print(f"Resultados para los números {num_a} y {num_b}:")
print(f"* Suma: {suma}")
print(f"* Resta: {resta}")
print(f"* Multiplicación: {multiplicacion}")
print(f"* División: {division}")

# Ejercicio 8 - Crear una función llamada calcular_imc(peso, altura) que reciba el peso en kilogramos y la altura en metros, y devuelva el índice de masa corporal (IMC). 
# Solicitar al usuario los datos y llamar a la fun- ción para mostrar el resultado con dos decimales.

def calcular_imc(peso, altura):
    return (peso / (altura ** 2))

peso = float(input("Ingrese un peso por favor: "))
altura = float(input("Ingrese una altura por favor: "))

imc = calcular_imc(peso, altura)

print(f"Tu indice de masa corporal es: {imc:.2f}")

# Ejercicio 9 Crear una función llamada celsius_a_fahrenheit(celsius) que reciba una 
# temperatura en grados Celsius y devuelva su equivalente en Fahrenheit. 
# Pedir al usuario la temperatura en Celsius y mostrar el resultado usando la función.

def celsius_a_fahrenheit(celsius):
    return (celsius * 1.8) + 32

celsius = float(input("Por favor ingresa una temperatura en celsius"))

fahrenheit = celsius_a_fahrenheit(celsius)

print(f"El resultado equivalente de {celsius} es {fahrenheit:.2f}")

# Ejercicio 10 - Crear una función llamada calcular_promedio(a, b, c) que reciba tres 
# números como parámetros y devuelva el promedio de ellos. Solicitar los 
# números al usuario y mostrar el resultado usando esta función.

def calcular_promedio(a, b, c):
    return ((a + b + c) / 3)

a = float(input("Ingresa el primer numero a calcular: "))
b = float(input("Ingresa el segundo numero a calcular: "))
c = float(input("Ingresa el tercer numero a calcular: "))

promedio = calcular_promedio(a, b, c)

print(f"El promedio de {a}, {b} y {c} es: {promedio}")
