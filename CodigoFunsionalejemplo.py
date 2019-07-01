import random


def buscar():
    contador = 0

    valores = []

    while True:

        contador += 1

        # Buscamos un numero aleatorio

        for i in range(1, 6):
            valores.append(random.randint(1, 5))

        print(valores)

        # Variable que determina el numero de valores que lleva la escalera

        numerosSeguidos = 0

        # Variable que contiene el numero anterior

        anterior = 0

        # Bucle para revisar los 6 valores obtenidos aleatoriamente

        for i in range(0, 5):

            if i > 0:

                # Si el valor actcual, es iguale al anterior mas uno

                # o

                # el valor es 1 y el anterior era el 6 y llevamos 3 numeros

                # consecutivos

                if valores[i] == anterior + 1 or (valores[i] == 1 and anterior == 6 and numerosSeguidos == 3):

                    numerosSeguidos += 1

                else:

                    # empezamos nuevamente

                    numerosSeguidos = 0

                # Guardamos el ultimo valor mostrado

                anterior = valores[i]

                # Si llevamos 5 numeros seguidos (empezamos por el 0) es que

                # tenemos la escalera

                if numerosSeguidos == 4:
                    return contador

            # La primera vez, obtenemos como valor anterior el primero

            if anterior == 0:
                anterior = valores[i]

        valores = []


contador = buscar()


print("Se ha conseguido una escalera en ", contador, "intentos
