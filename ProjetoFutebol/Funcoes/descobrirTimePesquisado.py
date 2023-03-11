def descobreTimePesquisado(lista,id):
    for linhas in range (len(lista)):
        if '"homeCompetitor"' in lista[linhas]:
            if id == lista[linhas+2]:
                return 0
        if '"awayCompetitor"' in lista[linhas]:
            if id == lista[linhas+2]:
                return 1