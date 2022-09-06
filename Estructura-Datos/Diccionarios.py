diccionario = {'nombre': 'alan', 'apellido': 'astorga', 'edad': 26}
diccionario2 = {1: 2}
print(diccionario)
print(diccionario.keys())
print(diccionario.values())
print(diccionario['apellido'])
diccionario['Peso'] = '90Kg'
print(diccionario)
diccionario['Peso'] = '100090Kg'
print(diccionario)
# Metodos
diccionario.pop('edad')
print(diccionario)
print(diccionario.get('Peso'))
diccionario.update(diccionario2)
print(diccionario)
diccionario.clear()
print(diccionario)
