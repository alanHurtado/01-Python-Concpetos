i = 0

while i < 10:
    i += 1
    print('Bucle while: {}'.format(i))

n = int(input('Número a multiplicar: '))
print(n)

i = 0

while i < 10:
    multi = i*n
    print('{} X {} = {}'.format(i, n, multi))
    i += 1
