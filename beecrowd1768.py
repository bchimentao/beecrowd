# 1768 - Árvore de Natal

while True:
    try:
        N = int(input())

        r = (N // 2) + 1
        for i in range(r, 0, -1):
          print(' ' * (i-1), end='')
          print('*' * (r-i+1), end='')
          print('*' * (r-i))
        print(' ' * (r-1), end='')
        print('*')
        print(' ' * (r-2), end='')
        print('***')
        print()
    except EOFError:
        break