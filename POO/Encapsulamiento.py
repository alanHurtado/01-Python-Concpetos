class A():
    def __init__(self) -> None:
        self.__contador = 0
        self._contadorDos = 0

    def incrementar(self):
        self.__contador += 1

    def cuenta(self):
        return self.__contador
    # Metodos GET ---Obtener

    def getContador(self):
        return self._contadorDos
    # O puede ser igual

    @property
    def contadorDos(self):
        return self._contadorDos

    # Metodos SET --Mandar o modificar atributo
    def setIncrementarContador(self):
        self._contadorDos += 1

    @contadorDos.setter
    def contadorDos(self, contadorDos):
        self._contadorDos = contadorDos


a = A()
print(a.cuenta())
a.incrementar()
print(a.cuenta())

# el encapsulamiento inpide acceser a los atributos de la clase
try:
    print(a.__contador)
except:
    print('no se puedo acceder al atributo por que esta encapsulado')

print('Modificar en encapsulamientos usando los metodos get y set')

# Metodos GET
a.setIncrementarContador()
print(a.getContador())
print('usando get con property', a.contadorDos)
a.contadorDos = 4
print('usando set con property', a.contadorDos)

