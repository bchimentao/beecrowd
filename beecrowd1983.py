# 1983 - O Escolhido

alunos_existentes = int(input())

notas_mec = {}

for _ in range(alunos_existentes):
    aluno, nota = map(float, input().split(' '))
    notas_mec[aluno] = nota

if max(notas_mec.values()) < 8:
    print('Minimum note not reached')
else:
    print(int(max(notas_mec, key=notas_mec.get)))