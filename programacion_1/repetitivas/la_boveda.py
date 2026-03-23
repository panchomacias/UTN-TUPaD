energia = 100
tiempo = 12
cerraduras_abiertas = 0
alarma = False
codigo_parcial = ""

nombre = input("Por favor ingresa tu nombre: ")
while not nombre.isalpha():
    print("Por favor solo ingresa letras")
    nombre = input("Por favor ingresa tu nombre: ")


anti_spam = 0

while energia > 0 and tiempo > 0 and cerraduras_abiertas < 3:
    print(f"Nombre jugador: {nombre}")
    print(f"Energia: {energia}")
    print(f"Tiempo: {tiempo}")
    print(f"Cerraduras abiertas: {cerraduras_abiertas}/3")
    print(f"Alarma activa: {alarma}")

    if alarma and tiempo <= 3:
        print("La alarma y el tiempo se acabaron")
        break

    choice = input(
        "Por favor elegir algua de las siguientes opciones:\n 1 - Forzar cerradura\n 2 - Hackear Panel\n 3 - Descansar\n "
    )
    while not choice.isdigit():
        print("Por favor debes ingresar un numero del menu")
        choice = input(
            "Por favor elegir algua de las siguientes opciones:\n 1 - Forzar cerradura\n 2 - Hackear Panel\n 3 - Descansar"
        )

    choice = int(choice)

    if choice == 1:
        anti_spam += 1

        if anti_spam >= 3:
            energia -= 20
            tiempo -= 2
            print(f"Se activo la alarma, dado que intentaste {anti_spam}/3 veces")
            alarma = True
        else:
            energia -= 20
            tiempo -= 2

            if energia < 40:
                print("Riesgo de alarma")
                numero = input("Tendras que elegir un numero del 1 al 3 ")
                while not numero.isdigit() and len(numero) > 1 and len(numero) <= 3:
                    print("Por favor elegir un numero entero del 1 al 3: ")
                    numero = input("Tendras que elegir un numero del 1 al 3 ")

                numero = int(numero)
                if numero == 3:
                    print("Se activará la Alarma")
                    alarma = True
                    break
            else:
                cerraduras_abiertas += 1
                print(f"Cerradura desbloqueada: {cerraduras_abiertas} / 3")

    elif choice == 2:
        anti_spam = 0

        energia -= 10
        tiempo -= 3

        for i in range(1, 5):
            codigo_parcial += "a".upper()
            print(f"Mostrando paso: {i} / 4. Codigo actual: {codigo_parcial}")

        if len(codigo_parcial) >= 8:
            cerraduras_abiertas += 1
            print(f"Cerradura desbloqueada: {cerraduras_abiertas} / 3")

    elif choice == 3:
        anti_spam = 0

        if energia <= 100:
            energia += 15

        tiempo -= 1

        if not alarma:
            energia -= 10

if cerraduras_abiertas >= 3:
    print("Victoria")
elif alarma and tiempo <= 3:
    print("Derrota")
elif energia <= 0 or tiempo <= 0:
    print("Derrota")
else:
    print("Misión abortada.")
