def pegarIdTimePesquisado(lista):
    for linhas in range (len(lista)):
        if 'competitors' in lista[linhas]:
            idTimePesquisado = lista[linhas+1]
            return idTimePesquisado