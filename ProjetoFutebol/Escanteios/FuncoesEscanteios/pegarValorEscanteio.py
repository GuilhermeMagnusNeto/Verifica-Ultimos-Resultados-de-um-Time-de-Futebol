def pegarValorEscanteio(lista):
    valoresEscanteios = []
    for item in range(len(lista)):
        if '"Escanteios"' == lista[item]:
            valoresEscanteios.append(lista[item+8])
    return valoresEscanteios