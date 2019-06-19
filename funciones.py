# 1  el print va dentro del def
# 2 append para pasar los nombres a una lista vacia.
# Funciones.
def jugadores():
    j = []  #J por jugadores.
    n = int(input('Ingrese el numero de jugadores para esta partida: '))
    for i in range(0,n):
        jugador = str(input('ingrese el nombre del jugador: '))
        j.append(jugador)
    for x in j:
        print(x)
jugadores()
