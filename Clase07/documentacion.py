#Para cada una de las siguientes funciones:

#Pensá cuál es el contrato de la función.
#Agregale la documentación adecuada.
#Comentá el código si te parece que aporta.
#Detectá si hay invariantes de ciclo y comentalo al final de la función

def valor_absoluto(num):
    '''Devuelve el valor absoluto de un número entero '''
    if num >= 0:
        return num
    else:
        return -num

def suma_pares(lista):
    '''Devuelve la suma de todos los elementos pares de una lista de números'''
    resultado = 0
    for elemento in lista:
        if elemento % 2 ==0:
            resultado += elemento
        else:
            resultado += 0
    return resultado

def veces(a, b):
    ''' Recibe dos numeros enteros.
    Devuelve la suma del numero a tantas veces como el numero b.  '''
    resultado = 0
    contador = b
    while contador != 0: 
        resultado += a
        contador -= 1
    return resultado
    
def collatz(n):
    resultado = 1

    while n!=1:
        if n % 2 == 0:
            n = n//2
        else:
            n = 3 * n + 1
        resultado += 1

    return resultado
