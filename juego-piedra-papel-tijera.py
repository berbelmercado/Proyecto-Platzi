# juego piedra papel o tijera
import random
# Declaramos las variables a utilizar en nuestro programa

rondas = 1
wins_user = 0
wins_computer = 0
choice_user = ''
choice = ["piedra", "papel", "tijera"]

# Declaramos while para ejecutar continuamente hasta que tengamos un ganador
while (True):
    print("********")
    print("RONDA ", rondas)
    print("********")
    print("\n______________")
    print("---> Victorias del usuario: ", wins_user)
    print("--->  Victorias de la máquina: ", wins_computer)
    print("______________")

    # solicitamos al usuario que ingrese su opción
    print("\nIngrese una de las siguientes opciones: Piedra,Papel o Tijera: ")
    choice_user = input()

    '''convertimos lo ingresado por el usuario en minusculas para que no importe la manera en 
    que sea ingresado el dato el sistema lo reconocerá igualmente'''
    choice_user = choice_user.lower()

    # evaluamos si el usuario ingresa "tijera" o "tijeras" el programa lo reconocerá igualmente
    if choice_user == "Tijeras":
        choice_user = "tijera"

    # Validamos que el dato ingresado por el usuario sea válida
    if choice_user not in choice:
        print("Por favor ingrese una opción válida")
        continue

    # El programa elegirá una opción para la máquina
    choice_computer = random.choice(choice)
    print("\n°°°°°°°°°°°°°°°°")
    print("Opción usuario : "+choice_user)
    print("Opción máquina: "+choice_computer)
    print("°°°°°°°°°°°°°°°°")
    # El programa determina quien gana y pierde la ronda según sus opciones
    if choice_user == "piedra" and choice_computer == "piedra":
        print("Empate")
    elif choice_user == "papel" and choice_computer == "papel":
        print("Empate")
    elif choice_user == "tijera" and choice_computer == "tijera":
        print("Empate")
    elif choice_user == "papel" and choice_computer == "piedra":
        wins_user += 1
        print("Usuario gana esta ronda")
    elif choice_user == "piedra" and choice_computer == "tijera":
        wins_user += 1
        print("Usuario gana esta ronda")
    elif choice_user == "tijera" and choice_computer == "papel":
        wins_user += 1
        print("Usuario gana esta ronta")
    else:
        print("La máquina gana esta ronda")
        wins_computer += 1

    if wins_computer == 2 or wins_user == 2:
        if wins_user == 2:
            print("-----------------")
            print("*******Usuario gana esta partida*******")
            print("-----------------")
        else:
            print("-----------------")
            print("*******La máquina gana esta partida*******")
            print("-----------------")
        break
    print("\n")
    rondas += 1
