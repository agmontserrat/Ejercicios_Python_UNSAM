# esfera.py
# Escribí un programa llamado esfera.py que le pida al usuario que ingrese por teclado el radio r de una esfera
# y calcule e imprima el volumen de la misma.
import math

radio = input("Ingrese el radio r de una esfera:")
volumen = (4 * math.pi * (int(radio) ** 3)) / 3
print("El volumen de una esfera de radio", radio, " es ",volumen)
