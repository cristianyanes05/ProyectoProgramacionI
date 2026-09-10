from random import randint


# FUNCIONES AUXILIARES
def codigo(matriz_torneo):
    puntos_totales = []

    for i in range(len(matriz_torneo)):
        puntos = sum([puntos for puntos in matriz_torneo[i] if puntos != -1])
        puntos_totales.append(puntos)

    return puntos_totales


# FUNCIONES PRINCIPALES
def ver_equipos(banco_general):
    print("\n---- Equipos ----\n")

    for equipo in banco_general:
        print(f'- {equipo}')

    input("\nPresiona ENTER para volver al menú...")


def agregar(agregados):
    if len(agregados) >= 6:
        print("\nYa hay 6 equipos agregados.")
        input("\nPresiona ENTER para volver al menú...")
        return agregados

    equipo_agregado = input("Ingrese el nombre del equipo (se pueden agregar hasta 6 equipos): ")

    while not equipo_agregado.isalpha() or equipo_agregado in agregados:

        if not equipo_agregado.isalpha():
            print("Entrada inválida, debe ingresar palabras sin números ni símbolos.\n")

        elif equipo_agregado in agregados:
            print("Ese equipo ya fue agregado anteriormente.\n")

        equipo_agregado = input("Ingrese el nombre del equipo: ")
        
    agregados.append(equipo_agregado)
    print(f"Equipo {equipo_agregado} agregado")

    return agregados


# ELEGIR EQUIPOS RANDOM
def eleccion(banco_general, agregados):
    faltantes = 6 - len(agregados)
    equipos_random = []

    while len(equipos_random) < faltantes:
        posicion = randint(0, len(banco_general) - 1)
        equipo = banco_general[posicion]

        if equipo not in equipos_random and equipo not in agregados:
            equipos_random.append(equipo)

    return equipos_random


# EQUIPOS FINALES
def equipos_finales(banco_general, agregados):
    equipos = []
    equipos_random = eleccion(banco_general, agregados)

    for equipo in equipos_random:
        equipos.append(equipo)

    for equipo in agregados:
        equipos.append(equipo)

    return equipos


# GENERAR CÓDIGOS
def generar_codigo(lista_equipos):
    codigo_equipos = []

    for equipo in lista_equipos:
        palabras = equipo.split()

        if len(palabras) >= 3:
            codigo = palabras[0][0] + palabras[1][0] + palabras[2][0]

        elif len(palabras) == 2:
            codigo = palabras[0][0] + palabras[1][0:2]

        else:
            codigo = palabras[0][:3]

        codigo_equipos.append(codigo.upper())

    return codigo_equipos


# ARMAR MATRIZ
def armar_matriz(equipos):
    partidas = 5
    matriz_total = [[-1 for i in range(partidas)] for i in range(len(equipos))]

    return matriz_total


# VISUALIZAR EQUIPOS
def visualizar_equipos_finales(equipos, codigos):
    print(f"{'Equipo':}", end=" | ")

    for i in range(5):
        print(f"{'Ronda ' + str(i + 1):}", end=" | ")
    
    print()
    print("-" * 70)

    for i in range(len(equipos)):
        print(f"{codigos[i]:}", end=" | ")

        for _ in range(5):
            print(f"{'-':}", end=" | ")
        print()

        


# SIMULAR SERIE
def simular_serie():
    puntos1 = 0
    puntos2 = 0

    while puntos1 < 2 and puntos2 < 2:
        resultado = randint(0, 1)

        if resultado == 1:
            puntos1 += 1

        else:
            puntos2 += 1

    return puntos1, puntos2


# CALCULAR PUNTOS
def calcular_puntos(equipo1, equipo2):
    if equipo1 == 2:

        if equipo2 == 0:
            return 6, 0

        else:
            return 3, 0

    else:
        if equipo1 == 0:
            return 0, 6

        else:
            return 0, 3


# SIMULAR TORNEO
def simular_torneo(equipos_finales, codigo_equipos):
    matriz_torneo = armar_matriz(equipos_finales)
    fixture = [
        [(0, 5), (1, 4), (2, 3)],
        [(0, 4), (5, 3), (1, 2)],
        [(0, 3), (4, 2), (5, 1)],
        [(0, 2), (3, 1), (4, 5)],
        [(0, 1), (2, 5), (3, 4)],
    ]

    for rondas in range(5):
        print(f"\n--- Ronda número {rondas + 1} ---")

        for partida in fixture[rondas]:
            equipo1 = partida[0]
            equipo2 = partida[1]

            print(f" {codigo_equipos[equipo1]} " f"vs " f"{codigo_equipos[equipo2]}")

            resultado1, resultado2 = simular_serie()

            print(f" {codigo_equipos[equipo1]} = " f"{resultado1}")

            print(f" {codigo_equipos[equipo2]} = " f"{resultado2}")

            puntos1, puntos2 = calcular_puntos(resultado1, resultado2)

            matriz_torneo[equipo1][rondas] = puntos1
            matriz_torneo[equipo2][rondas] = puntos2

            input("Presione ENTER para continuar....")

    print("\n--- Torneo Finalizado ---")
    input("--- Presione ENTER para volver al menú principal ---")

    return matriz_torneo


# TABLA GENERAL
def tabla_general(matriz_torneo, codigo_equipos):
    puntos_totales = codigo(matriz_torneo)

    indices = sorted(
        range(len(puntos_totales)), key=lambda i: puntos_totales[i], reverse=True
    )

    print("\n--- Tabla General ---")

    for posicion in range(len(indices)):
        i = indices[posicion]

        print(f"- {posicion + 1} {codigo_equipos[i]} = {puntos_totales[i]} puntos")

    input("\nPresione ENTER para volver al menú...")


# ESTADÍSTICAS
def estadistica_equipo(matriz_torneo, codigo_equipos):
    equipo = input("Elija el código del equipo: ").upper()
    posicion = -1

    for i in range(len(codigo_equipos)):
        if codigo_equipos[i] == equipo:
            posicion = i
            print(f"\n--- ESTADÍSTICAS DE {equipo} ---")

            for ronda in range(5):
                print(f"Ronda {ronda + 1}: {matriz_torneo[posicion][ronda]} puntos")

            series_ganadas = sum([1 for puntos in matriz_torneo[posicion] if puntos in (3, 6)])
            puntos_totales = sum([puntos for puntos in matriz_torneo[posicion] if puntos != -1])
            promedio = puntos_totales / 5
            
            print(f"\nPuntos totales: {puntos_totales}")
            print(f"Series ganadas: {series_ganadas}")
            print(f"Promedio de puntos: {promedio}")

    if posicion == -1:
        print("\nEse equipo no existe.")

    input("\nPresione ENTER para volver al menú...")


# PODIO
def podio(matriz_torneo, codigo_equipos):
    puntos_totales = codigo(matriz_torneo)
    indices = sorted(range(len(puntos_totales)), key=lambda i: puntos_totales[i], reverse=True)

    print("\n--- Podio ---")

    for posicion in range(3):
        i = indices[posicion]

        print(f"- {posicion + 1} {codigo_equipos[i]} = {puntos_totales[i]} puntos")

    input("\nPresione ENTER para volver al menú...")


# LÍDERES EN BARRIDAS
def lideres_barridas(matriz_torneo, codigo_equipos):
    cantidad_barridas = []

    for i in range(len(matriz_torneo)):
        barridas = sum([1 for puntos in matriz_torneo[i] if puntos == 6])
        cantidad_barridas.append(barridas)

    max_barridas = max(cantidad_barridas)
    print("\n--- Lideres de Barridas ---")

    if max_barridas == 0:
        print("Ningun equipo consiguió una barrida.")

    else:
        for i in range(len(codigo_equipos)):
            if cantidad_barridas[i] == max_barridas:
                print(f"{codigo_equipos[i]} = {cantidad_barridas[i]} barridas")

    input("\nPresione ENTER para volver al menu...")
