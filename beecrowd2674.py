# 2674 - Super Primos: Ativar!

from math import sqrt

def is_prime(number):
    if number in (2, 3, 5, 7):
        return True
    if number < 2 or number % 2 == 0:
        return False
    for i in range(3, int(sqrt(number)) + 1, 2):
        if number % i == 0:
            return False
    return True

def is_super_prime(number):
    while number >= 10:
        digit = number % 10
        number = number // 10
        if not is_prime(digit):
            return False
    return number in (2, 3, 5, 7)

while True:
    try:
        N = int(input())
        if not is_prime(N):
            print('Nada')
        else:
            if is_super_prime(N):
                print('Super')
            else:
                print('Primo')

    except EOFError:
        break