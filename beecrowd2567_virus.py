def let_max(lista_idades):

    # ordenando a lista de idades
    dias = lista_idades
    dias.sort()
    
    # se a quantidade de dias informados for ímpar, retira-se o termo do meio, 
    # pois ele será o pior positivo e o pior negativo para o cálculo
    if len(dias) % 2 != 0:
        termo_meio = (len(dias) // 2)
        del(dias[termo_meio])
    
    # divide a lista dias em dias positivos e dias negativos para que possamos
    # fazer a diferença entre os maiores números com os menores
    metade = int(len(dias) / 2)
    if metade == 1:
        dias_positivos = [dias[1]]
        dias_negativos = [dias[0]]
    else:
        dias_positivos = dias[metade::]
        dias_negativos = dias[0:metade]

    # lista com as diferenças
    dif_dias = [dias_positivos[i] - dias_negativos[i] for i in range(len(dias_positivos))]

    # retorna a soma da lista de diferenças
    return sum(dif_dias)

while True:
    try:
        # quantidade de vírus
        N = int(input())

        # idades dos vírus separados por espaço
        string = input()

        # tranformando a string em uma lista de inteiros
        string = string.split()
        idades = [int(i) for i in string]

        # print da maior letalidade
        print(let_max(idades))
    except EOFError:
        break