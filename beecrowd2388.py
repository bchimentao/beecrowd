# 2388 - Tacógrafo

N = int(input())

velocidade_total = 0

for n in range(N):
    T, V = map(int, input().split(' '))
    velocidade_total += T * V

print(velocidade_total)