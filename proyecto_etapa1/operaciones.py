from random import randint
import main
import datos 
agregados=[]

def ver_equipos():
    print(f'\n ----Equipos---- \n')
    for equipo in datos.banco_general:
        print(f'"{equipo}"')

    input("\nPresiona ENTER para volver al menú...")

def agregar():
    while True:
        equipo_agregado=input('ingrese el nombre del equipo: ')

        if equipo_agregado.isalpha():
            print(f'equipo {equipo_agregado} agregado')
            agregados.append(equipo_agregado)
            break
        else:
            print("Entrada inválida. Solo se permiten palabras sin números ni símbolos.\n")



    

            