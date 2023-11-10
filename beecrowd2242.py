# 2242 - Huaauhahhuahau

risada = input()

vogais = ['a', 'e', 'i', 'o', 'u']

risada_sem_con = []
for letra in risada:
    if letra in vogais:
        risada_sem_con.append(letra)

if risada_sem_con == risada_sem_con[::-1]:
    print('S')
else:
    print('N')