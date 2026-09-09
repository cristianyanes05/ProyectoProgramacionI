from random import randint
import datos 

# FUNCIONES AUXILIARES
def codigo(puntos_totales):
    
    for i in range(6):
        puntos= sum([ puntos for puntos in datos.matriz_torneo[i] if puntos !=1 ])

        puntos_totales.append(puntos)

    return puntos_totales



#FUNCIONES PRINCIPALES
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


#ELEGIR RANDOM LOS EQUIPOS DE BANCO_GENERAL
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


#JUNTA EQUIPOS DEL BANCO CON LOS ELEGIDOS POR EL USUARIO 
def equipos_finales():
    equipos_finales=[]

    equipo=eleccion()
    for i in equipo:
        equipos_finales.append(i)


    for i in datos.agregados:
        equipos_finales.append(i)

    return equipos_finales


#GENERA CODIGO DE LOS EQUIPOS FINALES
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



def visualizar_equipos_finales():
    equipos = equipos_finales()

    codigos= generar_codigo(equipos)

    matriz = armar_matriz(equipos)

    print(f"{'equipo':}", end=" | ")

    
    for i in range(5):
        print(f"{'Ronda ' + str(i + 1):}", end=" | ")

    print()
    print("-" * 90)

    for i in range(len(equipos)):
        print(f"{codigos[i]:}", end=" | ")

        for valor in matriz[i]:
            print(f"{valor:}", end=" | ")

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

    codigo(puntos_totales)

    indices= sorted(range(6), key=lambda i: puntos_totales[i], reverse=True)

    print('---Tabla General---')

    for posicion in range(6):

        i=indices[posicion]

        print(f'-{posicion+1}  {datos.codigo_equipos[i]} = {puntos_totales[i]}')

    

def estadistica_equipo():
    equipo= input('elija el codigo del equipo a ver el puntaje: ').upper()

    posicion=-1

    for i in range(len(datos.codigo_equipos)):

        if datos.codigo_equipos[i] == equipo:
            posicion = i

            print(f"\n---ESTADÍSTICAS DE {equipo} ----")

            for ronda in range(5):
                print(
                    f"Ronda {ronda + 1}: "
                    f"{datos.matriz_torneo[posicion][ronda]} puntos"
                )

            series_ganadas= sum([ 1 for puntos in datos.matriz_torneo[posicion] if puntos in (3,6)])

            puntos_totales= sum([
                puntos for puntos in datos.matriz_torneo[posicion] if puntos !=-1
            ])

            promedio= puntos_totales/5

            print(f"\n Puntos totales: {puntos_totales}")
            print(f"Series ganadas: {series_ganadas}")
            print(f"Promedio de puntos: {promedio:.2f}")

    if posicion == -1:
        print("Ese equipo no existe.")
        input("\nPresione ENTER para volver al menú...")
        return


def podio():
    puntos_totales=[]

    codigo(puntos_totales)
   
    indices= sorted(range(6), key=lambda i: puntos_totales[i], reverse=True)

    print('---Podio---')

    for posicion in range(3):

        i=indices[posicion]

        print(f'-{posicion+1}  {datos.codigo_equipos[i]} = {puntos_totales[i]}')
    

def lideres_barridas():

    cantidad_barridas=[]

    for i in range(6):

        barridas=sum([1 for puntos in datos.matriz_torneo[i] if puntos == 6])

        cantidad_barridas.append(barridas)

    max_barridas=max(cantidad_barridas)

    print('---Lideres de Barridas---')

    if max_barridas == 0:

        print("Ningún equipo consiguió una barrida.")

    else:

        for i in range(6):

            if cantidad_barridas[i] == max_barridas:

                print(f"{datos.codigo_equipos[i]}= {cantidad_barridas[i]} barridas")

    input("\nPresione ENTER para volver al menú...")