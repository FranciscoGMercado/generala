# Aca va el codigo de la base de datos. Ahora anda bien. Seguro se puede escribir mas compacto.
#  pero asi anda
import sqlite3

def jugadores():
    j = []  # J por jugadores.
    n = int(input('Ingrese el numero de jugadores para esta partida: '))
    for i in range(0, n):
        based = sqlite3.connect('generala.db')
        c = based.cursor()
        jugador = str(input('ingrese el nombre del jugador: '))
        c.execute('insert into jugadores(nombre_jugadores) values(?)', [jugador])
        based.commit()
        based.close()
        j.append(jugador)
    for s in j:
        print(s)

    '''La variable va entre corchetes como una lista, si no toma solo una letra,
    sobran las demas y tira un error'''
