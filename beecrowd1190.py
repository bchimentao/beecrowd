# 1190 - Área Direita

O = input('')

M = []

for i in range(12):
    linha = []
    for j in range(12):
        linha.append(float(input()))
    M.append(linha)


if O.upper() == 'S':
    soma = 0
    for n in range(5, 0, -1):
        try:
            for m in range(7, 12):
                soma += M[n][m + (5 - n)]
        except:
            continue
    for a in range(6, 11):
        try:
            for b in range(7, 12):
                soma += M[a][b + (a - 6)]
        except:
            continue

    print(f'{soma:.1f}')

elif O.upper() == 'S':
    soma = 0
    contador = 0
    for n in range(5, 0, -1):
        try:
            for m in range(7, 12):
                soma += M[n][m + (5 - n)]
                contador += 1
        except:
            continue
    for a in range(6, 11):
        try:
            for b in range(7, 12):
                soma += M[a][b + (a - 6)]
                contador += 1
        except:
            continue
    
    media = soma/contador
    print(f'{media:.1f}')

else:
    print('Não digitou S ou M!')