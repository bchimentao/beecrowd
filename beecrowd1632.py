# 1632 - Variações

T = int(input())

counter_T = 0

while counter_T < T:
    
    S = input()
    
    while not S.isalpha():
        S = input()
    
    counter = 1
    
    for i in S:
        if i == 'a' or i == 'A' \
        or i == 'e' or i == 'E' \
        or i == 'i' or i == 'I' \
        or i == 'o' or i == 'O' \
        or i == 's' or i == 'S':
            counter *= 3
        else:
            counter *= 2
    
    print(counter)
    
    counter_T += 1