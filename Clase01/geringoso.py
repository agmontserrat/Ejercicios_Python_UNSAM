# geringoso.py
# Usá una iteración sobre el string cadena para agregar la sílaba 'pa', 'pe', 'pi', 'po', o 'pu'
# según corresponda luego de cada vocal.

cadena = 'Geringoso'
capadepenapa = ''
for c in cadena:
    capadepenapa += c
    if c in 'aeiou':
        capadepenapa += 'p' + c

print(capadepenapa)
