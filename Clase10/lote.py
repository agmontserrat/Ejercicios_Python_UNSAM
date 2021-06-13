# Creá un archivo llamado lote.py y adentro definí una clase llamada Lote que represente 
# un lote de cajones de una misma fruta. 
# Definila de modo que cada instancia de la clase Lote (es decir, cada objeto lote) 
# tenga los atributos nombre, cajones, y precio. 

class Lote:
    def __init__(self, nombre, cajones, precio):
        self.nombre = nombre
        self.cajones = cajones
        self.precio = precio

    def __repr__(self):
        rep = f"Lote('{self.nombre}', {self.cajones}, {self.precio})"
        return rep

    def costo(self):
        return self.cajones * self.precio

    def vender(self, ncajones):
        self.cajones -= ncajones