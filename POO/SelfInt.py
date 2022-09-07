class Fabrica():
    marca = 'Xiaomi'
    color = 'negro'
    memoriaRam = 64
    almacenamiento = 256

    def llamar(self):
        self.marca = 'Motorola'


celular = Fabrica()
celular.color = 'Rojo'
print(celular.marca)
celular.llamar()
print(celular.marca)


class NuevaFabrica():
    # Contructor
    def __init__(self, marca, *colores, **especificaciones) -> None:
        self.marca = marca
        self.colores = colores
        self.especificaciones = especificaciones
        print('Ejecutando un metodo al asignar la clase en si es un constructor')

    def __str__(self) -> str:
        return 'El objeto es {}'.format(self.marca)

    # Destructor
    def __del__(self):
        print('El objeto {} ha sido destruido'.format(self.marca))


telefono = NuevaFabrica('Xiaomi', 'Rojo', 'Azul', 0,
                        memorira=86, procesador='Dragon', tamanio={'ancho': 98, 'alto': '98'})
print(telefono.marca)
print(telefono.colores)
print(telefono.especificaciones)
print(telefono.especificaciones)
print(telefono)
