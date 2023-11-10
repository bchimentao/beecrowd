# 2310 - Voleibol

N = int(input())

time = {
    'saque' : 0,
    'bloqueio' : 0,
    'ataque' : 0
}

sucesso = {
    'saque' : 0,
    'bloqueio' : 0,
    'ataque' : 0
}

for n in range (N):
    jogador = input()
    S, B, A = map(float, input().split(' '))
    S1, B1, A1 = map(float, input().split(' '))

    time['saque'] += S
    time['bloqueio'] += B
    time['ataque'] += A
    sucesso['saque'] += S1
    sucesso['bloqueio'] += B1
    sucesso['ataque'] += A1

percentual_saque = 100 * sucesso['saque'] / time['saque']
percentual_bloqueio = 100 * sucesso['bloqueio'] / time['bloqueio']
percentual_ataque = 100 * sucesso['ataque'] / time['ataque']

print(f'Pontos de Saque: {percentual_saque:.2f} %.')
print(f'Pontos de Bloqueio: {percentual_bloqueio:.2f} %.')
print(f'Pontos de Ataque: {percentual_ataque:.2f} %.')