def criaListaTimes(listaJogos, idPartidas, escanteios, cartoes, posseDeBola):
    listaTimes = []
    time = 0
    nomeTime2 = ""
    contador = 0
    contadorPosicao = 0
    contadorPosicaoPosse = 0

    for item in range(len(escanteios)):
        escanteios[item] = escanteios[item].replace('"', "")

    for item in range(len(cartoes)):
        cartoes[item] = cartoes[item].replace('"', "")

    for item in range(len(posseDeBola)):
        posseDeBola[item] = posseDeBola[item].replace('"', "")


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
                if (contador < len(escanteios)/2) and (contador< len(cartoes)/2) and (contador< len(posseDeBola)/2):
                    listaTimes.append("Escanteios:".lstrip())
                    listaTimes.append(escanteios[contadorPosicao])
                    listaTimes.append(escanteios[contadorPosicao+1])
                    listaTimes.append("Cartões:".lstrip())
                    listaTimes.append(cartoes[contadorPosicao])
                    listaTimes.append(cartoes[contadorPosicao+1])
                    listaTimes.append("Posse de Bola:".lstrip())
                    listaTimes.append(posseDeBola[contadorPosicaoPosse])
                    listaTimes.append(posseDeBola[contadorPosicaoPosse+2])
                else:
                    listaTimes.append("Escanteios:".lstrip())
                    listaTimes.append(0)
                    listaTimes.append(0)
                    listaTimes.append("Cartões:".lstrip())
                    listaTimes.append(0)
                    listaTimes.append(0)
                    listaTimes.append("Posse de Bola:".lstrip())
                    listaTimes.append(0)
                    listaTimes.append(0)
                contadorPosicao = contadorPosicao + 2
                contadorPosicaoPosse = contadorPosicaoPosse + 4
                contador = contador + 1

    return listaTimes