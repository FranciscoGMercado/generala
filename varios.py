import random

lista = ['jose', 'ricardo', 'laura', 'alberto', 'helena', 'vañeroa', 'estela', 'jorge', 'sergio','ricardo']

y = random.randint(0, 50)

dicc ={}

for x in lista:

    dicc.setdefault(x,y)

print(dicc)