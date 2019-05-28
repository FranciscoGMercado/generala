import sqlite3
import os

'''

base = sqlite3.connect('C:/Users/Maq301/PycharmProjects/generala/generala.db')
cursor = base.cursor()
'''
# Aclaracion para provar el push al testing.

dirname = os.path.dirname(__file__)
filename = os.path.join(dirname, 'generala.db')
print(filename)