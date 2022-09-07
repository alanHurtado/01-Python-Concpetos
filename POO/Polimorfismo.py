class Animales():
    def __init__(self, mensaje):
        self._mensaje = mensaje

    @property
    def mensaje(self):
        return self._mensaje

    def hablar(self):
        print('hola mundo ')


class Perro(Animales):
    def __init__(self, mensaje):
        super().__init__(mensaje)

    def hablar(self):
        print('Esto es polimorfimo')


mascota = Perro('Suky')

print(mascota.mensaje)
mascota.hablar()
print(mascota.mensaje)
