def pegarValorCartoes(lista):
    valoresCartoes = []
    for item in range(len(lista)):
        if '"Cartões amarelos"' == lista[item]:
            valoresCartoes.append(lista[item+8])
    return valoresCartoes