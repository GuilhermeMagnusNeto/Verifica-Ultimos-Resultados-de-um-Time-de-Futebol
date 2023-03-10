def criaListaTimes(listaJogos):
    listaTimes = []
    time = 0
    nomeTime2 = "";
    for linhas in range (len(listaJogos)):
        if 'name' == listaJogos[linhas]:
            if time==0:
                listaTimes.append(listaJogos[linhas+1])
                time = 1;
            else:
                nomeTime2 = listaJogos[linhas+1]
                time=0
        if 'score' == listaJogos[linhas]:
            if time==1:
                listaTimes.append(listaJogos[linhas+1])
            else:
                listaTimes.append("X")
                listaTimes.append(listaJogos[linhas+1])
                listaTimes.append(nomeTime2)
    return listaTimes