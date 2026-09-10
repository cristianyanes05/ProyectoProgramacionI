#Desarrollenperfil_equipo.pydentrodelacarpetacódigodelrepositorio.
#Elprogramadeberásolicitarelnombredelequipo,comisión,nombredecadaintegranteyrolinicialenelproyecto.
#•Normalizarlosnombrescontitle().
#•Convertirelnombredelequipoamayúsculas.
#•Informarlacantidaddecaracteresdelnombredelequipo.
#•Generarunasiglaconlainicialdecadapalabra.
#•Verificarsielnombredelequipocontienealmenosundígitorecorriendosuscaracteresyutilizandoisdigit().
#•Mostrartodalainformaciónmediantef-strings.
#•Mantenerlasoperacionesdeprocesamientodentrodefuncionesylaentrada/salidageneralenelprogramaprincipal.

defgenerar_sigla(nombre):
"""
Recibeelnombredelequipo,loseparaenpalabrasyextraelaprimera
letradecadaunapararetornarlasiglacompletaenmayúsculas.
"""
lista_palabras=nombre.split()
sigla=""
forpalabrainlista_palabras:
sigla=sigla+palabra[0]
returnsigla.upper()

defverificar_digito(nombre):
"""
RecorreloscaracteresdelnombreyretornaTruesiencuentra
almenosundígitonumérico,oFalseencasocontrario.
"""
forcaracterinnombre:
ifcaracter.isdigit():
returnTrue
returnFalse


print("\n")
cadena1="PERFILDELEQUIPO"
print(cadena1.center(50,"-"))
nombre_equipo=input("Ingresáelnombredelequipo:")
print("---")
comision=int(input("Ingresálacomisiónperteneciente:"))
print("---")
integrantes=input("Ingresáelnombredecadaintegrante:")
print("---")
rol_proyecto=input("Ingresáelrolinicialdecadaintegrante:")
print("---")
print("\n")
cadena2="RESULTADOS"
print(cadena2.center(50,"-"))
print(f"Nombresnormalizados:{integrantes.title()}")
print("---")
print(f"Nombredelequipoenmayúscula:{nombre_equipo.upper()}")
print("---")
print(f"Cantidaddecaracteresquecontieneelnombredelequipo:{len(nombre_equipo)}")
print("---")
sigla_equipo=generar_sigla(nombre_equipo)
print(f"Sigladelequipo:{sigla_equipo}")
print("---")
contiene_numero=verificar_digito(nombre_equipo)
ifcontiene_numero:
print(f"Elnombredelequipo{nombre_equipo}contienenumeros")
else:
print(f"Elnombredelequipo{nombre_equipo}notienenumeros")
print("---")


