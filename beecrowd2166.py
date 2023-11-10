# 2166 - Raiz Quadrada de 2

def raiz_quadada(n):

    if n == 0:
        return 2

    resultado = 2 + 1 / raiz_quadada(n-1)

    return resultado

numero = int(input())

print(f'{raiz_quadada(numero) - 1:.10f}')