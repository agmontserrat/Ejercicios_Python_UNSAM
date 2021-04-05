# El archivo Data/precios.csv contiene una serie de líneas con precios de venta de cajones en el mercado al que va el
# escribí una función buscar_precio(fruta) que busque en archivo ../Data/precios.csv el precio de determinada fruta
# (o verdura) y lo imprima en pantalla.
# Si la fruta no figura en el listado de precios, debe imprimir un mensaje que lo indique.


def buscar_precio(fruta):
    f = open('../Data/precios.csv', 'rt')
    encontre = False
    for line in f:
        elem = line.split(',')
        if elem[0] == fruta:
            print(f'El precio de un cajón de {fruta} es de {elem[1]}')
            encontre = True
    if not encontre:
        print(f'{fruta} no figura en el listado de precios')
    f.close()
