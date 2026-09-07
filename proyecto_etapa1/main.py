import operaciones as op
import datos

def mostrar_menu():
    print("\n===== TORNEO CS2 =====")
    print("1. Ver Banco General")
    print("2. Agregar Equipo")
    print("3. Simular Torneo")
    print("4. Tabla General")
    print("5. Estadísticas de Equipo")
    print("6. Podio")
    print("7. Líderes en Barridas")
    print("8. Resumen General")
    print("9. Salir")

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

 
            

        elif opcion=='9':
            print('\n Programa Finalizado')
            break

if __name__ == '__main__':
    main()