# 1581 - Conversa Internacional

N = int(input())

for n in range(N):
    K = int(input())
    lingua = []
    for k in range(K):
        lingua.append(input())
    if all(x == lingua[0] for x in lingua):
        print(lingua[0])
    else:
        print('ingles')