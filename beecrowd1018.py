# 1018 - Cédulas

numero = int(input(''))

while numero < 0 or numero > 1000000:
  numero = int(input(''))

print(numero)

cedulas_100 = numero // 100
dif_100 = numero % 100
print(f'{cedulas_100} nota(s) de R$ 100,00')

cedulas_50 = dif_100 // 50
dif_50 = dif_100 % 50
print(f'{cedulas_50} nota(s) de R$ 50,00')

cedulas_20 = dif_50 // 20
dif_20 = dif_50 % 20
print(f'{cedulas_20} nota(s) de R$ 20,00')

cedulas_10 = dif_20 // 10
dif_10 = dif_20 % 10
print(f'{cedulas_10} nota(s) de R$ 10,00')

cedulas_5 = dif_10 // 5
dif_5 = dif_10 % 5
print(f'{cedulas_5} nota(s) de R$ 5,00')

cedulas_2 = dif_5 // 2
dif_2 = dif_5 % 2
print(f'{cedulas_2} nota(s) de R$ 2,00')

cedulas_1 = dif_2
print(f'{cedulas_1} nota(s) de R$ 1,00')