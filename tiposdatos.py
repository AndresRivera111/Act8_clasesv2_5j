print ("Clases version 2. Andres Rivera")
# zona de clase
class Datos: 
    # el constructor funcion
    def __init__(self, estatura, peso):
        self.estatura = estatura
        self.peso = peso
    def mostrarDatos(self):
        print(f"Estatura: {self.estatura} m, Peso: {self.peso} kg")
    def miLista(self):
        celulares = ["Samsung", "Apple", "Xiaomi"]
        print(celulares)
        for c in celulares:
            print(c)
    def miTupla(self):
        colores = ("Rojo", "Azul", "Verde")
        print(colores)
        for m in colores:
            print(m)
    def miSet(self):
        albums = {"Genesis", "Exodo", "Incomodo"}
        print(albums)
        for a in albums:
            print(a)
    def miDiccionario(self):
        carro = {
            "Marca": "Chevrolet",
            "Modelo": "Camaro",
            "Año": 1979
            }
        print(carro) 
        for x, y in carro.items():
            print(x, y)      
#creacion del objeto
info = Datos(1.75, 70)

#utilizando el obj.
info.mostrarDatos()
print("Lista de marcas de celulares. Andres Rivera")
info.miLista()
print("Tupla de colores. Andres Rivera")
info.miTupla()
print("Set de albums. Andres Rivera")
info.miSet()
print("Diccionario de carros. Andres Rivera")
info.miDiccionario()
