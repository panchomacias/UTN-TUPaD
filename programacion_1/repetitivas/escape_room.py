nombre_gladiador = input("Ingresa el nombre del gladiador: ")
while not nombre_gladiador.isalpha():
    print("Error: Solo se permiten letras")
    nombre_gladiador = input("Ingresa el nombre del gladiador: ")

vida_gladiador = 100
vida_enemigo = 100
pociones_de_vida = 3
ataque_pesado = 15
dmg_enemigo = 12
turno_gladiador = True

while vida_gladiador > 0 and vida_enemigo > 0:
    if turno_gladiador:
        print(f"La vida del gladiador es: {vida_gladiador}")
        print(f"La vida del enemigo es: {vida_enemigo}")
        print(f"Las pociones restantes son: {pociones_de_vida}/3\n")

        choice = input(
            "Elige una de las siguientes opciones: \n1 - Ataque pesado\n 2 - Rafaga veloz\n 3 - Curar\n "
        )

        while not choice.isdigit():
            print("Error: solo se permiten numeros")
            choice = input(
                "Elige una de las siguientes opciones: 1 - Ataque pesado\n 2 - Rafaga veloz\n 3 - Curar\t "
            )

        choice = int(choice)

        if choice == 1:
            if vida_enemigo < 20:
                crit_dmg = ataque_pesado * 1.5
                vida_enemigo -= crit_dmg
                print(f"Atacaste al enemigo por {crit_dmg} puntos de daño")
            else:
                vida_enemigo -= ataque_pesado
                print(f"Atacaste al enemigo por {ataque_pesado} puntos de daño")

        elif choice == 2:
            for i in range(3):
                rafaga_veloz = 5
                vida_enemigo -= rafaga_veloz
                print(f"Atacaste al enemigo por {rafaga_veloz} puntos de daño")
        elif choice == 3:
            if pociones_de_vida > 0 and vida_gladiador < 100:
                cura = 30
                vida_gladiador = min(100, vida_gladiador + cura)
                pociones_de_vida -= 1
                print(
                    f"Te has curado {cura} puntos de vida, tu vida se encuentra en: {vida_gladiador}"
                )
            elif vida_gladiador >= 100:
                print(f"Tu vida se encuentra al máximo: {vida_gladiador}")
            else:
                print("No quedan pociones")

        print("Tu turno ha terminado\n")
        turno_gladiador = False

    elif not turno_gladiador:
        print("El enemigo te ataca")
        vida_gladiador -= 12
        print("El enemigo te atacó por 12 puntos de daño\n")
        turno_gladiador = True

if vida_gladiador > 0:
    print(f"VICTORIA! {nombre_gladiador} ha ganado la batalla")
else:
    print(f"DERROTA! {nombre_gladiador} ha caido en combate")
