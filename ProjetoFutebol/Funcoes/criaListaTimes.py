def criaListaTimes(listaJogos, idPartidas):
    listaTimes = []
    time = 0
    nomeTime2 = ""
    contador = 0
    for linhas in range (len(listaJogos)):
        if 'name' == listaJogos[linhas]:
            if time==0:
                listaTimes.append(idPartidas[contador])
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
                contador = contador + 1
                
    return listaTimes