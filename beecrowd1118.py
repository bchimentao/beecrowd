# 1118 - Várias Notas Com Validação

novo = 1

while novo == 1:

    nota1 =  float(input())
    while nota1 < 0 or nota1 > 10:
        print('nota invalida')
        nota1 =  float(input())
    
    nota2 =  float(input())
    while nota2 < 0 or nota2 > 10:
        print('nota invalida')
        nota2 =  float(input())
    
    media = (nota1 + nota2) / 2
    print(f'media = {media:.2f}')
    
    novo = int(input('novo calculo (1-sim 2-nao)\n'))
    while novo not in [1, 2]:
        novo = int(input('novo calculo (1-sim 2-nao)\n'))