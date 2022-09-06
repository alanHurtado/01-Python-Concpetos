
lista = ['hola', 'esto', 'es', 'una', 'lista', 2, 32]
print(type(lista))
# una lista es similar a un array
print(lista[3])
print(len(lista))
print('rebandado ejemplos:', lista[2:5], lista[:5], lista[4:])
# Las listas son mutables
lista[0] = 'nuevo valor'
print(lista)
# Metodos de listas
lista = [0, 1, 2, 3]
lista.append(7)
print(lista)
n = 0
for n in range(10):
    lista.append(n)
print(lista)
lista.insert(3, n)  # agrega dato en posición
print(lista)
print(lista.count(4))
# ordenar listas
lista.sort()
print(lista)
lista.reverse()
print(lista)
lista.pop()
print(lista)
print(lista.pop(), 'Elimino el ultimo valor')
lista.append('solo string')
print(lista)
lista.remove('solo string')
print('usando remove',lista)


