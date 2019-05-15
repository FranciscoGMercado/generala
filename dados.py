import random

dado_1 = []
dado_2 =[]
dado_3 =[]
dado_4 =[]
dado_5 =[]
def dados_L(n):
    lista = [0] * n
    for i in range(n):
        lista[i] = random.randint(0, 6)
    return  lista
n = 5
d = dados_L(n)
print(d)

def dados_D():
    dados = {'dado_1': 1, 'dado_2': 2, 'dado_3': 3, 'dado_4': 4, 'dado_5': 5}
    n = 5
    print(dados)
    dicc = dados_D()
    print(dicc)