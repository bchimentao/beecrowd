# 2694 - Problema com a Calculadora

N = int(input())

for i in range(N):
  a = input()
  soma = 0
  number = '0'
  
  for j in range(len(a)):

    if a[j].isnumeric():
      number = number + a[j]
      try:
        if not a[j+1].isnumeric():
          soma = soma + int(number)
          number = '0'
      except:
        soma = soma + int(number)
        number = '0'
        

  print(soma)