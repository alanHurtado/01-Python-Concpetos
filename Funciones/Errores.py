while True:
    try:
        edad: int(input('Ingresa su edad: '))
        print('tu edad es : ', edad)
        break
    except:
        print('Ingresaste un valor erroneo')
        break
    finally:
        print('La ejecución ha finalizado')
