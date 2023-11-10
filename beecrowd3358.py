# 3358 - Sobrenome Não é Fácil

N = int(input())

vogal = ['a', 'e', 'i', 'o', 'u']
for n in range(N):
  nome = input()
  facil = True
  for letra in range(len(nome)):
    try:
      if (nome[letra].lower() not in vogal) \
      and (nome[letra + 1].lower() not in vogal) \
      and (nome[letra + 2].lower() not in vogal):
        facil = False
        break
    except IndexError:
      break
    
  if facil:
    print(f'{nome} eh facil')
  else:
    print(f'{nome} nao eh facil')