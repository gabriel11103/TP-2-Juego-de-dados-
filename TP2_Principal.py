from TP2_Funciones import *

print("*" * 100)
print("\t\t\t\t\t\t\t\t\t\tBIENVENIDOS")
print("*" * 100)


j1 = input("ingrese el nombre del jugador 1: ")
j2 = input("ingrese el nombre del jugador 2: ")
#variables, contadores y banderas
x = puntaje_j1 = puntaje_j2 = 0
ronda_actual = 1
acu1 = acu2 = 0
empate = False
suma1 = 0
suma2 = 0
aciertos_j1 = 0
aciertos_j2 = 0
gano3seguidas = False
seguidas_j1 = 0
seguidas_j2 = 0
ganador_ronda = 0
#comienzo del juego
while x < 10:
    x = int(input("ingrese el objetivo \"debe ser mayor a 10\": "))

while puntaje_j1 < x and puntaje_j2 < x:
#jugador1
    print("*" * 100)
    print("comienza la ronda ", ronda_actual)
    print("*" * 100)

    print("turno de ", j1)
    puntaje_j1, acierto = ronda(puntaje_j1)
    if acierto == True:
        aciertos_j1 += 1
#jugador2
    print("*" * 100)
    print("turno de ", j2)
    puntaje_j2, acierto = ronda(puntaje_j2)
    if acierto == True:
        aciertos_j2 += 1

    print("*" * 100)
    print("puntajes de la ronda ", ronda_actual)
    print("el  puntaje de", j1, "es: ", puntaje_j1)
    print("el  puntaje de", j2, "es: ", puntaje_j2)
    #puntaje promedio
    suma1 += puntaje_j1
    suma2 += puntaje_j2
    #empate
    if puntaje_j1 == puntaje_j2:
        empate = True
        print("empataron")
    #ganador de cada ronda
    elif puntaje_j1 > puntaje_j2:
        print("el ganador de la ronda es ", j1)
        acu1 += 1
        ganador_ronda = j1
    else:
        print("el ganador de la ronda es ", j2)
        acu2 += 1
        ganador_ronda = j2
    #gano 3 seguidas
    if ganador_ronda == j1:
        seguidas_j2 = 0
        seguidas_j1 += 1
    else:
        seguidas_j1 = 0
        seguidas_j2 += 1
    if seguidas_j1 == 3:
        gano3seguidas = True
    elif seguidas_j2 == 3:
        gano3seguidas = True
    #cantidad de rondas
    ronda_actual += 1

print("*" * 100)
print("\t\t\t\t\t\t\t\t\t\tEl juego termino")
ganador = ganador(puntaje_j1, puntaje_j2, j1, j2, acu1, acu2)
if ganador == "empataron":
    print("Empataron")
else:
    print("EL GANADOR ES: ", ganador)
print("*" * 100)

print("\t\t\t\t\t\t\t\t\t\tEstadisticas")
#cantidad de rondas
print("la cantidad de rondas fue: ", ronda_actual - 1)
#empate
if empate == True:
    print("Hubo al menos un empate")
#puntaje promedio
puntaje_promedio_j1 = round(suma1 / ronda_actual, 2)
print("el puntaje promedio de ", j1, "es ", puntaje_promedio_j1)
puntaje_promedio_j2 = round(suma2 / ronda_actual, 2)
print("el puntaje promedio de ", j2, "es ", puntaje_promedio_j2)
#porcentaje de aciertos
porcentaje_j1 = (aciertos_j1 * 100)/ ronda_actual
print("el porcentaje de aciertos de ", j1, "es ", porcentaje_j1)
porcentaje_j2 = (aciertos_j2 * 100)/ ronda_actual
print("el porcentaje de aciertos de ", j2, "es ", porcentaje_j2)
if porcentaje_j1 > porcentaje_j2:
    porcentaje_ganador = j1
else:
    porcentaje_ganador = j2
if porcentaje_ganador == ganador:
    print("el ganador tuvo mayor cantidad de aciertos")
#gano 3 seguidas
if gano3seguidas == True:
    print("al menos un jugador gano 3 rondas seguidas")

