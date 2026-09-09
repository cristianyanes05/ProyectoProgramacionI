import operaciones as op
import datos

def mostrar_menu():
    print("\n===== TORNEO CS2 =====")
    print("1. Ver Banco General")
    print("2. Agregar Equipo")
    print("3. Visualizar Equipos Finales")
    print("4. Simular Torneo")
    print("5. Tabla General")
    print("6. Estadísticas de Equipo")
    print("7. Podio")
    print("8. Líderes en Barridas")
    print("9. Resumen General")
    print("10. Salir")

def main():
    while True:
        mostrar_menu()

        while True:
            opcion=input('seleccione una opcion: ')

            if opcion.isdigit():
                opcion=int(opcion)
                break

            print('debe ingresar un numero del 1 al 9 ')

        if opcion==1:
            op.ver_equipos()

        if opcion==2:
            op.agregar()

        if opcion==3:
            op.final()

        if opcion==4:
            op.simular_torneo()

        if opcion==5:
            op.tabla_general()

        if opcion==6:
            op.puntaje_especifico()


 
            

        elif opcion=='9':
            print('\n Programa Finalizado')
            break

if __name__ == '__main__':
    main()