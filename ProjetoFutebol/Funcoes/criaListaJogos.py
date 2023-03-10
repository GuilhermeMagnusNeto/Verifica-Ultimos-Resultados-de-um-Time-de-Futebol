import re
def criaListaJogos(lista):
    listaJogos = []
    for linhas in range (len(lista)):
        if '"homeCompetitor"' in lista[linhas]:
            jogoInicio = linhas
        if '"isHomeAwayInverted"' in lista[linhas]:
            jogoFinal = linhas;
            while (jogoInicio < jogoFinal):
                listaJogos.append(lista[jogoInicio]);
                jogoInicio = jogoInicio+1
    listaJogos = [re.sub(r'"','', i) for i in listaJogos]
    return listaJogos