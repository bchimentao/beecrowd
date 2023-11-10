# 1071 - Soma de Impares Consecutivos I

x = int(input())
y = int(input())

soma = 0
if x > y:
  r = range(y + 1, x)
elif x < y:
  r = range(x + 1, y)
else:
  r = range(0)
for i in r:
    if (i % 2) != 0:
        soma = soma + i

print(soma)