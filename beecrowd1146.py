# 1146 - Sequências Crescentes

x = int(input())

while x != 0:
    for i in range(x):
        if (i + 1) == x:
            print(i + 1)
        else:
            print(i + 1, end=' ')
    x = int(input())