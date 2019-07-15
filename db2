import sqlite3
from datetime import  datetime, date, time, timedelta

def juego():
    t = datetime.now()
    based = sqlite3.connect('generala.db')
    c = based.cursor()
    c.execute('insert into juego(momento) values(?)', [t])
    j = []  # J por jugadores.
    n = int(input('Ingrese el numero de jugadores para esta partida: '))
    for i in range(0, n):
        jugador = str(input('ingrese el nombre del jugador: '))
        c.execute('insert into jugadores(nombre_jugador) values(?)', [jugador])
        j.append(jugador)
    based.commit()
    based.close()
    for s in j:
        print(s)
