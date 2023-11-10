# 1079 - Médias Ponderadas

x = int(input())

count = 0
while count < x:
    a, b, c = map(float, input().split(' '))
    media_ponderada = (2 * a + 3 * b + 5 * c) / 10
    print(f"{media_ponderada:.1f}")
    count  += 1