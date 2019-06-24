import sqlite3
import time

def juego():
    t = int(time.time())
    based = sqlite3.connect('generala.db')
    c = based.cursor()
    c.execute('insert into juego(momento) values(?)', [t])
    j = []  # J por jugadores.
    n = int(input('Ingrese el numero de jugadores para esta partida: '))
    for i in range(0, n):
        jugador = str(input('ingrese el nombre del jugador: '))
        c.execute('insert into jugadores(nombre_jugadores) values(?)', [jugador])
        j.append(jugador)
    based.commit()
    based.close()
    for s in j:
        print(s)
