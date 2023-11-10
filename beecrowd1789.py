# 1789 - A Corrida de Lesmas

while True:
    try:
        L = input()
        lesmas = input().split(' ')
        
        mais_veloz = max(float(i) for i in lesmas)
        
        if mais_veloz < 10:
          print(1)
        elif 10 < mais_veloz < 20:
          print(2)
        else:
          print(3)
    except EOFError:
        break