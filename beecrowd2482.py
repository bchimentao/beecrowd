# 2482 - Etiquetas de Noel

N = int(input())

mensagens = {}

for _ in range(N):
    indice = input()
    mensagens[indice] = input()

M = int(input())

# pessoas = {}

for _ in range(M):
    nome = input()
    idioma = input()
    print(nome)
    print(mensagens[idioma])
    print()