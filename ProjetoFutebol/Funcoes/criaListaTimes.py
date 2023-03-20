def criaListaTimes(listaJogos, idPartidas, escanteios, cartoes):
    listaTimes = []
    time = 0
    nomeTime2 = ""
    contador = 0
    contadorEscanteios = 0
    for item in range(len(escanteios)):
        escanteios[item] = escanteios[item].replace('"', "")
    for item in range(len(cartoes)):
        cartoes[item] = cartoes[item].replace('"', "")
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
                if (contador < len(escanteios)/2) and (contador< len(cartoes)/2):
                    listaTimes.append("Escanteios:".lstrip())
                    listaTimes.append(escanteios[contadorEscanteios])
                    listaTimes.append(escanteios[contadorEscanteios+1])
                    listaTimes.append("Cartões:".lstrip())
                    listaTimes.append(cartoes[contadorEscanteios])
                    listaTimes.append(cartoes[contadorEscanteios+1])
                else:
                    listaTimes.append("Escanteios:".lstrip())
                    listaTimes.append(0)
                    listaTimes.append(0)
                    listaTimes.append("Cartões:".lstrip())
                    listaTimes.append(0)
                    listaTimes.append(0)
                contadorEscanteios = contadorEscanteios + 2
                contador = contador + 1
    return listaTimes