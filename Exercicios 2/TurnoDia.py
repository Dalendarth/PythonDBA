turno = input('Digite o turno em que você estuda: '
              ' D- Diurno'
              ' V- Vespetino'
              ' N- Noturno').lower()

if turno == 'd':
    print('Bom dia!')
    if turno == 'v':
        print('Boa tarde!')
        if turno == 'n':
            print('Boa noite!')
        else:
            print('Entrada invalida!')
    else:
        print('Entrada invalida!')
else:
    print('Entrada invalida!')