nombre_operador = input("Por favor ingresa el nombre del operador: ")
while not nombre_operador.isalpha():
    print("El nombre tiene que tener solo letras")
    nombre_operador = input("Por favor ingresa tu nombre: ")

lunes_1 = ""
lunes_2 = ""
lunes_3 = ""
lunes_4 = ""
martes_1 = ""
martes_2 = ""
martes_3 = ""

contador_lunes = 0
contador_martes = 0

while True:
    print("Selecciona una de las opciones: ")
    print("1 - Reservar turno")
    print("2 - Cancelar turno")
    print("3 - Ver agenda del dia")
    print("4 - Ver resumen general")
    print("5 - Cerrar sistema")

    seleccion = input("Selecciona 1, 2, 3, 4 o 5, por favor: ")
    while not seleccion.isdigit():
        print("Por favor escribi un numero del 1 al cinco ")
        seleccion = input("Selecciona 1, 2, 3, 4 o 5, por favor: ")

    seleccion = int(seleccion)

    if seleccion == 1:
        dia = input("Tendras que elegir un dia: 1 para Lunes o 2 para Martes ")
        while not dia.isdigit():
            print("Por favor elige un numero entero del 1 al 2")
            dia = input("Tendras que elegir un dia: 1 para Lunes o 2 para Martes ")

        dia = int(dia)

        nombre_paciente = input("Porfavor ingresa el nombre del paciente: ")
        while not nombre_paciente.isalpha():
            print("El nombre tiene que tener solo letras")
            nombre_paciente = input("Por favor ingresa tu nombre: ")

        if dia == 1:
            if (
                nombre_paciente == lunes_1
                or nombre_paciente == lunes_2
                or nombre_paciente == lunes_3
                or nombre_paciente == lunes_4
            ):
                print(
                    f"{nombre_paciente} Ya tiene un turno para el dia lunes reservado"
                )

            elif contador_lunes < 4:
                if lunes_1 == "":
                    lunes_1 = nombre_paciente
                elif lunes_2 == "":
                    lunes_2 = nombre_paciente
                elif lunes_3 == "":
                    lunes_3 = nombre_paciente
                else:
                    lunes_4 = nombre_paciente

                contador_lunes += 1
                print(f"Turno reservado para {nombre_paciente}")
            else:
                print("Ya no hay mas turnos disponibles para el lunes")

        elif dia == 2:
            if (
                nombre_paciente == martes_1
                or nombre_paciente == martes_2
                or nombre_paciente == martes_3
            ):
                print(
                    f"{nombre_paciente} Ya tiene un turno para el dia Martes reservado"
                )

            elif contador_martes < 3:
                if martes_1 == "":
                    martes_1 = nombre_paciente
                elif martes_2 == "":
                    martes_2 = nombre_paciente
                else:
                    martes_3 = nombre_paciente

                contador_martes += 1
                print(f"Turno reservado para {nombre_paciente}")
            else:
                print("Ya no hay mas turnos disponibles para el Martes")

    elif seleccion == 2:
        dia = input("Tendras que elegir un dia: 1 para Lunes o 2 para Martes ")
        while not dia.isdigit():
            print("Por favor elige un numero entero del 1 al 2")
            dia = input("Tendras que elegir un dia: 1 para Lunes o 2 para Martes ")

        dia = int(dia)

        if dia == 1:
            nombre_paciente = input("Porfavor ingresa el nombre del paciente: ")
            while not nombre_paciente.isalpha():
                print("El nombre tiene que tener solo letras")
                nombre_paciente = input("Por favor ingresa tu nombre: ")

            if lunes_1 == nombre_paciente:
                lunes_1 = ""
                contador_lunes -= 1
                print("Turno cancelado el dia lunes")
            elif lunes_2 == nombre_paciente:
                lunes_2 = ""
                contador_lunes -= 1
                print("Turno cancelado en Lunes")
                print("Turno cancelado el dia lunes")
            elif lunes_3 == nombre_paciente:
                lunes_3 = ""
                contador_lunes -= 1
                print("Turno cancelado en Lunes")
                print("Turno cancelado el dia lunes")
            elif lunes_4 == nombre_paciente:
                lunes_4 = ""
                contador_lunes -= 1
                print("Turno cancelado el dia lunes")
            else:
                print(f"El paciente {nombre_paciente} no tiene turno el lunes")

        elif dia == 2:
            nombre_paciente = input("Porfavor ingresa el nombre del paciente: ")
            while not nombre_paciente.isalpha():
                print("El nombre tiene que tener solo letras")
                nombre_paciente = input("Por favor ingresa tu nombre: ")

            if martes_1 == nombre_paciente:
                martes_1 = ""
                contador_martes -= 1
                print("Turno cancelado el dia martes")
            elif martes_2 == nombre_paciente:
                martes_2 = ""
                contador_martes -= 1
                print("Turno cancelado el dia martes")

            elif martes_3 == nombre_paciente:
                martes_3 = ""
                contador_martes -= 1
                print("Turno cancelado el dia martes")
            else:
                print("El paciente no tiene turno el Martes")

    elif seleccion == 3:
        dia = input("Tendras que elegir un dia: 1 para Lunes o 2 para Martes")
        while not dia.isdigit():
            print("Por favor elige un numero entero del 1 al 2")
            dia = input("Tendras que elegir un dia: 1 para Lunes o 2 para Martes")

        dia = int(dia)

        if dia == 1:
            print("Mostrando los turnos del dia Lunes: ")
            if lunes_1 == "":
                print("Turno 1: Disponible")
            else:
                print(f"Turno 1:  {lunes_1}\n")

            if lunes_2 == "":
                print("Turno 2: Disponible")
            else:
                print(f"Turno 2:  {lunes_2}\n")

            if lunes_3 == "":
                print("Turno 3: Disponible")

            else:
                print(f"Turno 3:  {lunes_3}\n")

            if lunes_4 == "":
                print("Turno 4: Disponible")

            else:
                print(f"Turno 4:  {lunes_4}\n")

        elif dia == 2:
            print("Mostrando los turnos del dia Martes: ")
            if martes_1 == "":
                print("Turno 1: Disponible")
            else:
                print(f"Turno 1: {martes_1}")

            if martes_2 == "":
                print("Turno 2: Disponible")
            else:
                print(f"Turno 2: {martes_2}")

            if martes_3 == "":
                print("Turno 3: Disponible")
            else:
                print(f"Turno 3: {martes_3}")

    elif seleccion == 4:
        print("Resumen general: ")
        print(
            f"Turnos ocupados para Lunes: {contador_lunes} y turnos disponibles {4 - contador_lunes}"
        )
        print(
            f"Turnos ocupados para Martes: {contador_martes} y turnos disponibles {3 - contador_martes}"
        )

        if contador_lunes > contador_martes:
            print("El Lunes tiene más turnos ocupados")
        elif contador_martes > contador_lunes:
            print("El Martes tiene más turnos ocupados")
        else:
            print("Ambos días tienen la misma cantidad de turnos")

    elif seleccion == 5:
        break
