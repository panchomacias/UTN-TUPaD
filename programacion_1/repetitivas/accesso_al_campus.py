import random

intentos = 1
login = False

while intentos <= 3 and not login:
    user = input("Ingresa tu user: ")
    password = input("Ingresa tu password: ")

    if user == "alumno" and password == "python123":
        login = True
        print(
            f"Intento: {intentos} / 3 - Usuario: {user}\n Clave: {password}\n Accesso Confirmado\n"
        )

        while True:
            # Menu interactivo
            print(
                "Menu interactivo - Por favor elige alguna de las opciones a continuación:\n"
            )
            print("1 - Ver estado de inscripción")
            print("2 - Cambiar clave")
            print("3 - Mostrar mensaje Motivacional")
            print("4 - Salir")

            eleccion = input("Elige 1, 2, 3 o 4, por favor: \t")

            # Validacion is digit() y que el numero elegido se encuentra en el rango
            while not eleccion.isdigit() or int(eleccion) not in range(1, 5):
                print("Por favor selecciona un un numero de las opciones provistas.")
                eleccion = input("Elige 1, 2, 3 o 4, por favor: ")

            # Pasamos la eleccion a integer para comparar en el if statement
            eleccion = int(eleccion)

            if eleccion == 1:
                print("\nInscripto")

            elif eleccion == 2:
                contraseña_cambiada = False
                while not contraseña_cambiada:
                    contraseña = input("Por favor elige una nueva contraseña: ")

                    while len(contraseña) < 6:
                        contraseña = input(
                            "Por favor elige una contraseña que sea mayor a seis: "
                        )

                    confirmacion_contraseña = input(
                        "Por favor confirma la contraseña: "
                    )

                    if contraseña == confirmacion_contraseña:
                        print("Password correctamente cambiado \n")
                        contraseña_cambiada = True
                    else:
                        print("Los password no coinciden \n")

            elif eleccion == 3:
                # Importo random para usar diferentes frases
                frases_motivadores = [
                    "La vida es como andar en bicicleta. Para mantener el equilibrio, debes seguir moviéndote",
                    "Una persona que nunca ha cometido un error nunca ha intentado algo nuevo",
                    "No pretendamos que las cosas cambien, si siempre hacemos lo mismo",
                    "La mente es como un paracaídas... solo funciona si la tenemos abierta",
                ]
                print(f"\n{random.choice(frases_motivadores)} \n")

            else:
                break
    else:
        print(
            f"Itento: {intentos} / 3 - Usuario: {user}\n Clave: {password}\n Error: credenciales invalidas"
        )

    intentos += 1

if not login:
    print("Máximo tres intentos, cuenta bloqueada")
