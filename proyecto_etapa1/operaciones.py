from random import randint
import datos 

def ver_equipos():
    print(f'\n ----Equipos---- \n')
    for equipo in datos.banco_general:
        print(f'"{equipo}"')

    input("\nPresiona ENTER para volver al menú...")


def agregar():
    while True:
        equipo_agregado=input('ingrese el nombre del equipo (podes agregar hasta 6 equipos): ') 

        if equipo_agregado.isalpha():
            if equipo_agregado not in datos.agregados:
                print(f'equipo {equipo_agregado} agregado')
                datos.agregados.append(equipo_agregado)
                break
            else:
                print("Ese equipo ya fue agregado anteriormente.\n")
            
        else:
            print("Entrada inválida. Solo se permiten palabras sin números ni símbolos.\n")


def eleccion():
    faltantes=6-len(datos.agregados)

    while len(datos.eleccion) > faltantes:
        datos.eleccion.pop()


    while len(datos.eleccion) < faltantes:
        posicion=randint(0,(len(datos.banco_general)-1))
        equipo=datos.banco_general[posicion]

        if equipo not in datos.eleccion and equipo not in datos.agregados:
            datos.eleccion.append(equipo)

    return datos.eleccion


def equipos_finales():
    equipos_totales=[]

    equipo=eleccion()
    for i in equipo:
        equipos_totales.append(i)


    for i in datos.agregados:
        equipos_totales.append(i)

    return equipos_totales


def generar_codigo(lista_equipos):

    datos.codigo_equipos=[]

    for i in lista_equipos: 
        palabras = i.split()

        if len(palabras) >= 3:
            codigo = palabras[0][0] + palabras[1][0] + palabras[2][0]
        elif len(palabras) == 2:
            codigo = palabras[0][0] + palabras[1][0:2]
        else:
            codigo = palabras[0][:3]

        datos.codigo_equipos.append(codigo.upper())

    return datos.codigo_equipos


def armar_matriz(equipos):
    partidas=5
    matriz_total=[[-1 for _ in range(partidas)] for _ in range(len(equipos))]
    return matriz_total


def final():
    equipos = equipos_finales()

    codigos= generar_codigo(equipos)

    matriz = armar_matriz(equipos)

    print(f"{'equipo':^12}", end=" | ")

    
    for i in range(5):
        print(f"{'Ronda ' + str(i + 1):^12}", end=" | ")

    print()
    print("-" * 90)

    for i in range(len(equipos)):
        print(f"{codigos[i]:^12}", end=" | ")

        for valor in matriz[i]:
            print(f"{valor:^12}", end=" | ")

        print()

#TORNEO 
def simular_serie():
    puntos1=0
    puntos2=0

    while puntos1 < 2 and puntos2 < 2:
        resultado=randint(0,1)

        if resultado==1:
            puntos1+=1
        else:
            puntos2+=1

    return puntos1, puntos2        

def calcular_puntos(equipo1,equipo2):

    if equipo1 == 2:
        if equipo2 == 0:
            return 6,0
        
        else: 
            return 3,0

    else:
        if equipo1 == 0:
            return 0,6

        else:
            return 0,3
    

def simular_torneo():
    datos.equipos_finales = equipos_finales()
    datos.codigo_equipos = generar_codigo(datos.equipos_finales)
    datos.matriz_torneo = armar_matriz(datos.equipos_finales)

    fixture = [
        [(0, 5), (1, 4), (2, 3)],
        [(0, 4), (5, 3), (1, 2)],
        [(0, 3), (4, 2), (5, 1)],
        [(0, 2), (3, 1), (4, 5)],
        [(0, 1), (2, 5), (3, 4)]
    ]

    for rondas in range(5):
        print(f'\n ---Ronda numero {rondas + 1}---')

        for partida in fixture[rondas]:

            equipo1= partida[0]
            equipo2= partida[1]

            print(f' {datos.codigo_equipos[equipo1]} vs {datos.codigo_equipos[equipo2]}')

            puntos1,puntos2=simular_serie()

            print(f' {datos.codigo_equipos[equipo1]} = {puntos1}')
            print(f' {datos.codigo_equipos[equipo2]} = {puntos2}')

            puntos1,puntos2= calcular_puntos(puntos1,puntos2)

            datos.matriz_torneo[equipo1][rondas] = puntos1
            datos.matriz_torneo[equipo2][rondas] = puntos2

            input(f'Presione ENTER para continuar....')

    datos.torneo_simulado = True

    print('---Torneo Finalizado---')
    input(f'---Presione ENTER volver al menú principal---')


# PUNTAJES Y RANKINGS
def tabla_general():
    puntos_totales=[]

    for i in range(6):
        puntos= sum([ puntos for puntos in datos.matriz_torneo[i] if puntos !=1 ])

        puntos_totales.append(puntos)

    

def puntaje_especifico():
    equipo= input('elija el equipo a ver el puntaje: ')

    if equipo not in datos.equipos_finales:
        print(f'el equipo {equipo} no se encuentra dentro de la matriz ')

    else:


            