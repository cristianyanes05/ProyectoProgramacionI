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
    matriz_total=[[0 for _ in range(partidas)] for _ in range(len(equipos))]
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

#def simular_torneo():

            