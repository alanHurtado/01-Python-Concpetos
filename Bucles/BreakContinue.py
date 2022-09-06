for i in range(10, 100, 5):
    print(i)
    if i == 50:
        break
for i in range(10, 100, 5):
    if i == 50:
      print('salto')
      continue
    print(i, 'en si salta')
