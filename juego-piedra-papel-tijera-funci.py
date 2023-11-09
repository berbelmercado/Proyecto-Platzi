# juego piedra papel o tijera trabajado en funciones (programación estructurada)
# librería para escoger datos aleatorios
import random

# Declaramos las funciones a utilizar en nuestro programa


def choice_computer():
    '''función que contiene las opciones de la máquina'''
    choice = ["piedra", "papel", "tijera"]
    return choice


def seleccion_opciones_sistema(opciones):
    ''' función que escoje una opción disponible al azar'''
    opciones = random.choice(opciones)
    return opciones


def solicitud_opcion_usuario():
    '''función que solicita al usuario las opciones'''
    print("\nIngrese una de las siguientes opciones: Piedra,Papel o Tijera: ")
    choice_user = input()
    return choice_user


def opcion_usuario_minusculas(choice_user):
    '''convertimos lo ingresado por el usuario en minusculas para que no importe la manera en 
    que sea ingresado el dato el sistema lo reconocerá igualmente'''
    choice_user = choice_user.lower()
    return choice_user


def choice_error(choice_user):
    '''función que permite controlar las opciones ingresadas por el usuario'''
    if choice_user not in choice_computer():
        print("------------------Por favor ingrese una opción válida ------------------")
        control = False
    else:
        control = True
    return control


def print_usuario(choice_user):
    '''función que imprime la opción ingresada por el usuario'''
    print("\n°°°°°°°°°°°°°°°°")
    print("Opción usuario : "+choice_user)


def print_sistema(choice_sistema):
    ''' función que imprime la opción tomada por el sistema'''
    print("Opción máquina: "+choice_sistema)
    print("\n°°°°°°°°°°°°°°°°")


def control_victorias(punto_usuario, punto_sistema, victoria_usuario, victoria_sistema, ronda):
    '''función que controla las victorias en el juego'''
    if punto_usuario == 1 and punto_sistema == 0:
        victoria_usuario += 1
    elif punto_usuario == 0 and punto_sistema == 1:
        victoria_sistema += 1
    elif punto_usuario == 0 and punto_sistema == 0:
        victoria_usuario += 0
        victoria_sistema += 0
    ronda += 1
    return victoria_usuario, victoria_sistema, ronda


def victoria_ronda(punto_usuario, punto_sistema):
    '''función que muestra que participante gana la ronda'''
    if punto_usuario == 1 and punto_sistema == 0:
        print("el usuario gana esta ronda")
    elif punto_usuario == 0 and punto_sistema == 0:
        print("Empate")
    else:
        print("El sistema gana esta ronda")


def logica_juego(choice_user, choices_computer):
    '''función que contiene la lógica del juego'''
    wins_user = 0
    wins_computer = 0
    if choice_user == "piedra" and choices_computer == "piedra":
        wins_user = 0
        wins_computer = 0
    elif choice_user == "papel" and choices_computer == "papel":
        wins_user = 0
        wins_computer = 0
    elif choice_user == "tijera" and choices_computer == "tijera":
        wins_user = 0
        wins_computer = 0
    elif choice_user == "papel" and choices_computer == "piedra":
        wins_user = 1
    elif choice_user == "piedra" and choices_computer == "tijera":
        wins_user = 1
    elif choice_user == "tijera" and choices_computer == "papel":
        wins_user = 1
    else:
        wins_computer = 1
    return wins_user, wins_computer


def score(puntos_usuario, puntos_sistema, rondas):
    '''fución ue muestra el score del juego'''
    print("********")
    print("RONDA ", rondas)
    print("********")
    print("\n______________")
    print("---> Victorias del usuario: ", puntos_usuario)
    print("--->  Victorias de la máquina: ", puntos_sistema)
    print("______________")


def cierre_partida(victoria_sistema, victoria_usuario):
    '''controla cierre de partida'''
    cierre = False
    if victoria_usuario == 3 or victoria_sistema == 3:
        cierre = True
    return cierre


def imprimir_ganador(victoria_sistema, victoria_usuario, cierre):
    '''función que indica quien ganó la ronda'''
    if cierre is True:
        if victoria_sistema > victoria_usuario:
            print(
                "***************************El sistema gana esta partida********************")
        else:
            print(
                "***************************El Usuario gana esta partida********************")


CIERRE_RONDA = False
RONDA = 1
CONTEO_VICTORIA_USUARIO = 0
CONEO_VICTORIA_SISTEMA = 0

while CIERRE_RONDA is False:
    # mostramos el Score inicial
    score(CONTEO_VICTORIA_USUARIO, CONEO_VICTORIA_SISTEMA, RONDA)

    # solicitamos al usuario que ingrese su opción
    OPCION_USUARIO = solicitud_opcion_usuario()

    # transformamos todos los Strings en minúnsculas
    OPCION_USUARIO = opcion_usuario_minusculas(OPCION_USUARIO)

    # ratificamos que el dato ingresado por el usuario sea válido
    CONTROL = choice_error(OPCION_USUARIO)
    while CONTROL is False:
        OPCION_USUARIO = solicitud_opcion_usuario()
        CONTROL = choice_error(OPCION_USUARIO)

    # El programa elegirá una opción para la máquina
    OPCION_SISTEMA = seleccion_opciones_sistema(choice_computer())

    # se imprimen las opciones de ambos jugadores
    print_usuario(OPCION_USUARIO)
    print_sistema(OPCION_SISTEMA)
    # El programa determina quien gana y pierde la ronda según sus opciones
    VICTORIA_USUARIO, VICTORIA_SISTEMA = logica_juego(
        OPCION_USUARIO, OPCION_SISTEMA)

    # se muestra el ganador de la ronda
    victoria_ronda(VICTORIA_USUARIO, VICTORIA_SISTEMA)

    CONTEO_VICTORIA_USUARIO, CONEO_VICTORIA_SISTEMA, RONDA = control_victorias(
        VICTORIA_USUARIO, VICTORIA_SISTEMA, CONTEO_VICTORIA_USUARIO, CONEO_VICTORIA_SISTEMA, RONDA)

    # controlamos el cierre de la partida
    CIERRE_RONDA = cierre_partida(
        CONEO_VICTORIA_SISTEMA, CONTEO_VICTORIA_USUARIO)

    imprimir_ganador(CONEO_VICTORIA_SISTEMA,
                     CONTEO_VICTORIA_USUARIO, CIERRE_RONDA)
