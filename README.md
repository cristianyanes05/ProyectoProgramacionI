Integrantes:
    Encina, Leonel
    Vazquez, Gonzalo
    Yanes, Cristian

Probelma:
    Creacion de Sistema para administrar un torneo de un videojuego (Cs2).

Alcance del Proyecto:
   El proyecto consiste en desarrollar un sistema por consola para gestionar un torneo de eSports. 
El programa estara dividido en 2 archivos, uno el main.py y otro llamado funciones.py
Los puntos de las rondas serán ingresados aleatoriamente utilizando la librería random.

Mensaje de bienvenida al menú del torneo
Menú:
 opciones:
ver equipos iniciales
agregar un equipo
simular torneo
Buscar equipo
puntaje maximo
puntaje promedio por equipo (otra matriz)
fin

ver equipos iniciales: 
llama a la funcion VisualizarEquipos(), se imprimirán mediante f-strings en pantalla los equipos a seleccionar aleatoriamente
agregar equipo:
llama a la función AgregarEquipo()
Buscar equipo:
llama a la función BuscarEquipo(), permite buscar un equipo en el torneo y ver las estadísticas en el torneo
simular torneo:
llama a la función SimularTorneo()
fin:
Finaliza la ejecución del programa

En el main.py estaran:
Los datos de entrada:
Cantidad máxima de equipos en el torneo
Cantidad máxima de rondas en el torneo
Datos de procesamiento:
La matriz va a estar hecha automáticamente con los datos que ingreso el usuario 
Agregar un nuevo equipo al torneo mediante un input
Salida de datos con f-strings

En el Funciones.py estaran:
funciones lambda
función VisualizarEquipos(), permite ver la cantidad y nombres de equipos seleccionados para el torneo
función SimularTorneo(), permite ver la matriz completa del torneo, con el puntaje final y posición en el torneo
función BuscarEquipo(), guarda en una matriz los nombres y las estadísticas de los equipos participantes
función AgregarEquipo(), permite al usuario agregar un equipo nuevo, validando que el nombre sea normalizado y con un mínimo de caracteres

Uso de tuplas para guardar puntajes y donde se ubican los equipos a seleccionar de forma random
Entre 2 equipos, se define qu	ien gana por mejor de 3
Validación de datos random, que un equipo tenga si o si 2 rondas ganadas para ganar la ronda general

Lo que omitimos:
uso de try/catch para manejo de errores

