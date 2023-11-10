# 1134 - Tipo de Combustível

combustivel = {
    'Alcool' : 0,
    'Gasolina' : 0,
    'Diesel' : 0,
    }

x = int(input())

while x <= 0 or x > 4:
    x = int(input())

while x != 4:
    if x == 1:
        combustivel['Alcool'] += 1
    elif x == 2:
        combustivel['Gasolina'] += 1
    else:
        combustivel['Diesel'] += 1
    
    x = int(input())
    while x <= 0 or x > 4:
        x = int(input())

print('MUITO OBRIGADO')
for i, j in combustivel.items():
    print(f'{i}: {j}')