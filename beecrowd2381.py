# 2381 - Lista de Chamada

N, K = map(int, input().split(' '))

alunos = [input() for _ in range(N)]

alunos.sort()

print(alunos[K-1])