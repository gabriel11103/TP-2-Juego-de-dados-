__author__ = 'grupo nn 1k12'

#FUNCION TIRA DE DADOS Y MUESTRA
def tirar_dado():
    import random
    return random.randint(1,6)
def tirardados():
    d1 = tirar_dado()
    d2 = tirar_dado()
    d3 = tirar_dado()
    print("VALORES:", d1,d2,d3)
    return d1,d2,d3
#FUNCION PARIDAD
def paridadElegida():
    may, men, puntaje = 0, 0, 0
    print("Elegir paridad de la suma total de sus dados, apuesta su puntaje")
    paridad = int(input("0 si elige PAR , 1 si elige IMPAR\nInserte paridad:"))
    d1, d2, d3 = tirardados()
    suma = d1 + d2 + d3
    if suma % 2 == paridad:
        print("Es la paridad elegida, se le sumará a su puntaje el valor del dado mayor")
        if d2 < d1 > d3:
            may = d1
        if d1 < d2 > d3:
            may = d2
        if d2 < d3 > d1:
            may = d3
        puntaje= puntaje + may
        if d1 % 2 == paridad and d2 % 2 == paridad and d3 % 2 == paridad:
            puntaje = puntaje * 2
            print("Duplica su puntaje ya que cada dado es de la paridad elegida")
    else:
        print("No es de la paridad elegida, se le resta el dado de menor valor")
        if d2 > d1 < d3:
            men = d1
        if d1 > d2 < d3:
            men = d2
        if d1 > d3 < d2:
            men = d3
        puntaje = puntaje - men
    return puntaje
def juego():
    # TÍTULO,PRESENTACIÓN.
    print("#" * 40)
    print("BIENVENIDOS AL JUEGO DE DADOS: DOS TRES")
    print("#" * 40)
    # INGRESA NOMBRES
    player1 = input("inserte nombre player1: ")
    player2 = input("inserte nombre player2: ")
    # RONDA 2
    print("ROUND 2")
    print("COMIENZA PLAYER 1:", player1)
    # TIRA DE DADOS-LLAMA A FUNCION Y MUESTRA VALORES
    puntaje1 = paridadElegida()
    print("Puntaje para Player1:", puntaje1)
    # TURNO PLAYER 2:
    print("TURNO PLAYER 2:", player2)
    # TIRA DE DADOS, MUESTRA VALORES A LLAMADO DE FUNCIÓN
    puntaje2 = paridadElegida()
    print("Puntaje para Player2:", puntaje2)
    # FINAL DE RONDA
    print("-" * 50)
    print("FINALIZA RONDA\n*PUNTAJES*")
    print(player1, ": ", puntaje1)
    print(player2, ": ", puntaje2)
    if puntaje1 == puntaje2:
        print("EMPATE")
    elif puntaje1 > puntaje2:
        print("GANÓ:", player1)
    else:
        print("GANÓ:", player2)
    print("-" * 50)
juego()
