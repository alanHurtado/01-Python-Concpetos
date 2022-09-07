class Fabrica():
    marca = 'Xiaomi'
    color = 'negro'
    memoriaRam = 64
    almacenamiento = 256

    def llamar(self, mensaje):
        return mensaje


celular = Fabrica()
print(celular.llamar('Hola como estas'))
celular.color='Rojo'
print(celular.marca)
