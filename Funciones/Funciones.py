def imprimir():
    print('Se imprimio un mensaje des una funcion')


def imprimirAlgo(x):
    print(x)


def tabla(num, rango):
    for i in range(1, rango):
        multi = i * num
        print('{} X {} = {}'.format(num, i, multi))


imprimir()
imprimirAlgo('Esto es lo que mando a imprimir')
tabla(2, 9)
