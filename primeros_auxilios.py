llego = 0
estimulos = int(input('Responde a Estímulos?\n1.Si    2.No\n'))
if estimulos == 1:
    print('Valorar la necesidad de llevarlo al hospital más cercano')
elif estimulos == 2:
    print('Abrir la vía Aeréa')
    respira = int(input('Respira?\n1.Si    2.No\n'))
    if respira == 1:
        print('Permitirle posición de suficiente ventilación')
    elif respira == 2:
        print('Administrar 5 ventilaciones y llamar a Ambulancia')
        while llego != 1:
            signos = int(input('Signos de Vida?\n1.Si    2.No\n'))
            if signos == 1:
                print('Reevaluar a la espera de la ambulancia')
                llego = int(input('Llegó la Ambulancia?\n1.Si    2.No\n'))
            elif signos == 2:
                print('Administrar Compresiones Torácicas hasta que llegue ambulancia')
                llego = int(input('Llegó la Ambulancia?\n1.Si    2.No\n'))
            else:
                print('Respuesta Erronea')
    else:
        print('Respuesta Erronea')
else:
    print('Respuesta Erronea')

print('Fin')
