from traceback import print_tb


class Animales():
    def __init__(self, nombre) -> None:
        self._nombre = nombre

    @property
    def nombre(self):
        return self._nombre

    def habla(self):
        print('Yo soy un animal por ende no hablo')


class Perro(Animales):
    def __init__(self, nombre, raza) -> None:
        super().__init__(nombre)
        self._raza = raza

    @property
    def raza(self):
        return self._raza


suky = Perro('suky', 'Maltes')
print('la herencia esta aqí')
suky.habla()
print(suky.nombre)
print(suky.raza)
