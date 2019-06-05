# Aca va el codigo de la base de datos.Aca
import sqlite3
def base_datos():
    base = sqlite3.connect('C:/Users/Maq301/PycharmProjects/generala')
    c = base.cursor()

def jugadores():
    j = []  # J por jugadores.
    n = int(input('Ingrese el numero de jugadores para esta partida: '))
    for i in range(0, n):
        jugador = str(input('ingrese el nombre del jugador: '))
        j.append(jugador)
    for s in j:
        print(s)
    based = sqlite3.connect('generala.db')
    c = based.cursor()
    '''La variable va entre corchetes como una lista, si no toma solo una letra,
    sobran las demas y tira un error'''
    c.execute('insert into jugadores(nombre_jugadores) values(?)', [j])
    based.commit()
    based.close()
