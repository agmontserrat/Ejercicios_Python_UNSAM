import random
from collections import Counter 

def es_generala(tirada):
    """Devuelve True si y solo si los cinco dados de la lista tirada son iguales"""
    valores=set(tirada) #Convierto a set para eliminar repeticiones
    if len(valores)==1: #Si hay un solo elemento, todos los numeros son iguales
        #print("Es generala")
        return True
    #print("no es generala")
    return False

def numero_random():
    numero = random.randint(1,6)
    return numero


def tirar(lista):
    """Devuelve una lista con cinco dados generados aleatoriamente. """
    while len(lista) != 5:
        lista.append(numero_random())
    return(lista)


def jugada():
    """Proceso de una jugada de generala, donde se tienen hasta 3 tiros para sacar todos los numeros iguaeles"""
    repeticiones = 2 #Cantidad de veces que podemos volver a tirar
    tirada = tirar([])
    es = es_generala(tirada)
    print(tirada)
    while es == False and repeticiones > 0:
        if len(set(tirada))==5: #Si nos tocaron todos diferentes
            tirada = tirar([])
            repeticiones -= 1 #Decremento
        else: #Si tenemos que elegir con qué numero quedarnos
            mas_repetido = Counter(tirada).most_common()[0][0] #Mas repetido
            for i in range(len(tirada)): # Por cada indice de la lista, me fijo si es el mas repetido y si no, saco un numero nuevo.
                if tirada[i] != mas_repetido:
                    tirada[i]= numero_random()
            repeticiones -= 1 #Decremento
        es = es_generala(tirada)        
        print ('repeticiones: ',repeticiones, 'tirada',tirada)
    return es
        


N=1000
jugada()
G = sum([jugada() for i in range(N)])
prob= G/N
print(f'Jugué {N} veces, de las cuales {G} saqué generala.')
print(f'Podemos estimar la probabilidad de sacar generala mediante {prob:.6f}.')
