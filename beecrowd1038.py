# 1038 - Lanche

cachorro_quente = 4
x_salada = 4.5
x_bacon = 5
torrada_simples = 2
refrigerante = 1.5
total = 0

codigo, quant = map(int, input().split(' '))

while codigo < 0 or codigo > 5:
  codigo, quant = map(int, input().split(' '))

if codigo == 1:
  total = cachorro_quente * quant
elif codigo == 2:
  total = x_salada * quant
elif codigo == 3:
  total = x_bacon * quant
elif codigo == 4:
  total = torrada_simples * quant
elif codigo == 5:
  total = refrigerante * quant

print(f'Total: R$ {total:.2f}')