# Desarrollen perfil_equipo.py dentro de la carpeta código del repositorio. 
# El programa deberá solicitar el nombre del equipo, comisión, nombre de cada integrante y rol inicial en el proyecto.
# • Normalizar los nombres con title().
# • Convertir el nombre del equipo a mayúsculas.
# • Informar la cantidad de caracteres del nombre del equipo.
# • Generar una sigla con la inicial de cada palabra.
# • Verificar si el nombre del equipo contiene al menos un dígito recorriendo sus caracteres y utilizando isdigit().
# • Mostrar toda la información mediante f-strings.
# • Mantener las operaciones de procesamiento dentro de funciones y la entrada/salida general en el programa principal.

def generar_sigla(nombre):
    """ 
    Recibe el nombre del equipo, lo separa en palabras y extrae la primera 
    letra de cada una para retornar la sigla completa en mayúsculas.
    """
    lista_palabras = nombre.split()
    sigla = ""
    for palabra in lista_palabras:
        sigla = sigla + palabra[0]
    return sigla.upper()

def verificar_digito(nombre):
    """
    Recorre los caracteres del nombre y retorna True si encuentra 
    al menos un dígito numérico, o False en caso contrario.
    """
    for caracter in nombre:
        if caracter.isdigit():
            return True
    return False


print("\n")
cadena1= "PERFIL DEL EQUIPO"
print(cadena1.center(50, "-"))
nombre_equipo = input("Ingresá el nombre del equipo: ")
print("---")
comision = int(input("Ingresá la comisión perteneciente: "))
print("---")
integrantes = input("Ingresá el nombre de cada integrante: ")
print("---")
rol_proyecto = input("Ingresá el rol inicial de cada integrante: ")
print("---")
print("\n")
cadena2= "RESULTADOS"
print(cadena2.center(50, "-"))
print(f"Nombres normalizados: {integrantes.title()}")
print("---")
print(f"Nombre del equipo en mayúscula: {nombre_equipo.upper()}")
print("---")
print(f"Candidad de caracteres que contiene el nombre del equipo: {len(nombre_equipo)}")
print("---")
sigla_equipo = generar_sigla(nombre_equipo)
print(f"Sigla del equipo: {sigla_equipo}")
print("---")
contiene_numero = verificar_digito(nombre_equipo) 
if contiene_numero:
    print (f"El nombre del equipo {nombre_equipo} contiene numeros")
else:
    print(f"El nombre del equipo {nombre_equipo} no tiene numeros")
print("---")


