from random import randint
import datos 

def ver_equipos():
    print(f'\n ----Equipos---- \n')
    for equipo in datos.banco_general:
        print(f'"{equipo}"')

    input("\nPresiona ENTER para volver al menú...")

def agregar():
    while True:
        equipo_agregado=input('ingrese el nombre del equipo: ')

        if equipo_agregado.isalpha():
            if equipo_agregado not in datos.agregados:
                print(f'equipo {equipo_agregado} agregado')
                datos.agregados.append(equipo_agregado)
                break
            else:
                print("Ese equipo ya fue agregado anteriormente.\n")
            
        else:
            print("Entrada inválida. Solo se permiten palabras sin números ni símbolos.\n")


def equipos_finales():
    equipos_totales=[]

    faltantes=6-len(datos.agregados)
    while len(equipos_totales) < faltantes:
        posicion=randint(0,(len(datos.banco_general)-1))
        equipo=datos.banco_general[posicion]

        if equipo not in equipos_totales and equipo not in datos.agregados:
            equipos_totales.append(equipo)

    for i in datos.agregados:
        equipos_totales.append(i)

    return equipos_totales

def armar_matriz(equipos):
    partidas=15
    matriz_total=[[0 for _ in range(partidas)] for _ in range(len(equipos))]
    return matriz_total

def final():
    equipos = equipos_finales()
    matriz = armar_matriz(equipos)

    print(f"{'equipo':^12}", end=" | ")

    
    for i in range(15):
        print(f"{'Ronda ' + str(i + 1):^12}", end=" | ")

    print()
    print("-" * 220)

    for i in range(len(equipos)):
        print(f"{equipos[i]:^12}", end=" | ")

        for valor in matriz[i]:
            print(f"{valor:^12}", end=" | ")

        print()

#def simular_torneo():

            