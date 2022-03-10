def paridad():
    eleccion = None
    while eleccion != "1" or eleccion != "2":
        print("""
        elija una opcion
            opciones
            1-Impar
            2-Par
        """)
        eleccion = input("ingrese su eleccion: ")
        if eleccion == "1" or eleccion == "2":
            if eleccion == "1":
                resultado = 1
            else:
                resultado = 0
            return resultado
        else:
            print("eleccion incorrecta")

def tirar_dados():
    import random
    d1 = random.randint(1, 6)
    d2 = random.randint(1, 6)
    d3 = random.randint(1, 6)
    print("dado1: ", d1)
    print("dado2: ", d2)
    print("dado3: ", d3)
    return d1, d2, d3


def paridad_compu():
    dado1, dado2, dado3 = tirar_dados()
    resto = (dado1 + dado2 + dado3) % 2
    return resto, dado1, dado2, dado3


def ronda(puntaje):
    acierto = False
    eleccion = paridad()
    paridad_computadora, dado1, dado2, dado3 = paridad_compu()
    if eleccion == paridad_computadora:
        if dado1 > dado2 and dado1 > dado3:
            mayor = dado1
        elif dado2 > dado3:
            mayor = dado2
        else:
            mayor = dado3
        print("la suma de los dados es igual a tu eleccion, sumaste ", mayor, "puntos")
        acierto = True
        puntaje = puntaje + mayor
        if (dado1 % 2) == eleccion and (dado2 % 2) == eleccion and (dado3 % 2) == eleccion:
            print("todos los dados eran iguales a tu eleccion, duplicaste tu puntaje")
            puntaje *= 2
    else:
        if dado1 < dado2 and dado1 < dado3:
            menor = dado1
        elif dado2 < dado3:
            menor = dado2
        else:
            menor = dado3
        print("la suma de los dados es distinta a tu eleccion, restaste ", menor, "puntos")
        puntaje -= menor
    return puntaje, acierto

def ganador(puntaje_j1, puntaje_j2, j1, j2, acu1, acu2):
    if puntaje_j1 != puntaje_j2:
        if puntaje_j1 > puntaje_j2:
            ganador = j1
        else:
            ganador = j2
        return ganador
    else:
        if acu1 == acu2:
            print("Empataron")
            empate = "empataron"
            return empate
        elif acu2 > acu1:
            print("EL GANADOR ES: ", j1)
            ganador = j1
        else:
            print("EL GANADOR ES: ",j2)
            ganador = j2
        return ganador
