import random

def listaAleatorios(n):
      lista = [0] * n
      for i in range(n):
          lista[i] = random.randint(0, 6)
      return lista

n= 5
aleatorios=listaAleatorios(n)
print(aleatorios)



