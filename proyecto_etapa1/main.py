# main.py → acá se maneja el menú, la entrada del usuario y llamamos a los otros archivos.
import operaciones as op
import datos


# imprime en pantalla las opciones del menú
def mostrar_menu():
    print("\n--- Torneo CS2 ---")
    print("1. Ver banco general")
    print("2. Agregar equipo")
    print("3. Visualizar equipos finales")
    print("4. Simular torneo")
    print("5. Tabla general")
    print("6. Estadísticas de equipo")
    print("7. Podio")
    print("8. Líderes en barridas")
    print("-" * 20)
    print("9. Salir")


# carga la lista con los equipos que ya vienen guardados
def main():
    banco_general = datos.obtener_banco_general()
    # variables con listas vacías para guardar los datos y la matriz a medida que avanza el programa
    agregados = []
    equipos_finales = []
    codigo_equipos = []
    matriz_torneo = []

    # bandera para saber si ya se simuló el torneo o no
    torneo_simulado = False

    opcion = 0

    # bucle while para mantener el menú abierto hasta que aprieten 9
    while opcion != 9:

        mostrar_menu()

        opcion = input("Seleccione una opcion: ")
        # valida que metan un número del 1 al 9 y no se rompa
        while not opcion.isdigit() or int(opcion) < 1 or int(opcion) > 9:
            print("Debe ingresar un numero del 1 al 9.")
            opcion = input("Seleccione una opcion: ")

        opcion = int(opcion)

        if opcion == 1:
            # suma un nuevo equipo a la lista
            op.ver_equipos(banco_general)

        elif opcion == 2:
            agregados = op.agregar(agregados)
        # Registra y guarda nuevos equipos ingresados manualmente
        elif opcion == 3:
            equipos_finales = op.equipos_finales(banco_general, agregados)

            codigo_equipos = op.generar_codigo(equipos_finales)

            op.visualizar_equipos_finales(equipos_finales, codigo_equipos)

        elif opcion == 4:
            if len(equipos_finales) == 6:
                matriz_torneo = op.simular_torneo(equipos_finales, codigo_equipos)

                torneo_simulado = True

            else:
                print("\nPrimero debe visualizar los equipos finales.")
        # de la opcion 5 a la 8 se valida que el torneo ya haya sido simulado (torneo_simulado == True)
        elif opcion == 5:
            if torneo_simulado:
                op.tabla_general(matriz_torneo, codigo_equipos)

            else:
                print("\nPrimero debe simular el torneo.")

        elif opcion == 6:
            if torneo_simulado:
                op.estadistica_equipo(matriz_torneo, codigo_equipos)

            else:
                print("\nPrimero debe simular el torneo.")

        elif opcion == 7:
            if torneo_simulado:
                op.podio(matriz_torneo, codigo_equipos)

            else:
                print("\nPrimero debe simular el torneo.")

        elif opcion == 8:
            if torneo_simulado:
                op.lideres_barridas(matriz_torneo, codigo_equipos)

            else:
                print("\nPrimero debe simular el torneo.")

        elif opcion == 9:
            print("\nPrograma Finalizado")


# arranca el programa llamando a main()
if __name__ == "__main__":
    main()
