# 1248 - Plano de Dieta

N = int(input())

for n in range(N):
    dieta = input()
    cheater = False
    
    cafe = input()
    almoco = input()

    for c in cafe:
        if c in dieta:
            dieta = dieta.replace(c, '')
        else:
            cheater = True

    for a in almoco:
        if a in dieta:
            dieta = dieta.replace(a, '')
        else:
            cheater = True

    if cheater:
        print('CHEATER')
    else:
        print(''.join(sorted(dieta)))