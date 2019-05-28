import sqlite3
import os

'''


'''
# Aclaracion para provar el push al testing.

dirname = os.path.dirname(__file__)
filename = os.path.join(dirname, 'generala.db')
base = sqlite3.connect(filename)
cursor = base.cursor()

print(filename)