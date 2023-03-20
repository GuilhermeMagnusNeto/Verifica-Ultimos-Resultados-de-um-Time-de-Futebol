def calcularMediaEscanteios(timePesquisado):
    #armazena informações do arquivo na variavel partidas
    with open('dados.txt', 'r', encoding="utf-8") as arq:
        partidas = arq.readlines()
        for i in range(len(partidas)):
            partidas[i]=partidas[i].replace("\n", "")
    arq.close();

    #variáveis das médias
    mediaEscanteiosCasa = 0
    mediaEscanteiosFora = 0
    mediaEscanteiosTotal = 0
    mediaEscanteiosSofridosCasa = 0
    mediaEscanteiosSofridosFora = 0
    mediaEscanteiosSofridosTotal = 0
    #variáveis total de escanteios feitos
    totalEscanteiosCasa = 0
    totalEscanteiosFora = 0
    totalEscanteios = 0
    #variáveis total de escanteios sofridos
    totalEscanteiosSofridosCasa = 0
    totalEscanteiosSofridosFora = 0
    totalEscanteiosSofridos = 0
    #variável para quantidade de jogos em casa e fora
    quantidadeJogosCasa = 0
    quantidadeJogosFora = 0
    quantidadeJogosTotal = 0

    # descobrindo o nome do time que foi pesquisado
    if timePesquisado == 0:
        nomeTimePesquisado = partidas[1]
    elif timePesquisado == 1:
        nomeTimePesquisado = partidas[5]
        
    for contador in range(len(partidas)):
        if contador%13 == 0:
            if partidas[contador+1] == nomeTimePesquisado:
                totalEscanteiosCasa = totalEscanteiosCasa+float(partidas[contador+7])
                totalEscanteiosSofridosCasa = totalEscanteiosSofridosCasa+float(partidas[contador+8])
                quantidadeJogosCasa = quantidadeJogosCasa+1
            else:
                totalEscanteiosFora = totalEscanteiosFora+float(partidas[contador+8])
                totalEscanteiosSofridosFora = totalEscanteiosSofridosFora+float(partidas[contador+7])
                quantidadeJogosFora = quantidadeJogosFora+1

    #calculo dos totais de escanteios
    totalEscanteios = totalEscanteiosFora + totalEscanteiosCasa
    totalEscanteiosSofridos = totalEscanteiosSofridosFora + totalEscanteiosSofridosCasa
    quantidadeJogosTotal = quantidadeJogosFora+quantidadeJogosCasa
    #calculo da media de escanteios feitos
    mediaEscanteiosCasa = totalEscanteiosCasa/quantidadeJogosCasa
    mediaEscanteiosFora = totalEscanteiosFora/quantidadeJogosFora
    mediaEscanteiosTotal = totalEscanteios/quantidadeJogosTotal
    #calculo da media de escanteios sofridos
    mediaEscanteiosSofridosCasa = totalEscanteiosSofridosCasa/quantidadeJogosCasa
    mediaEscanteiosSofridosFora = totalEscanteiosSofridosFora/quantidadeJogosFora
    mediaEscanteiosSofridosTotal = totalEscanteiosSofridos/quantidadeJogosTotal

    print("\n********Cálculo de médias de escanteios em casa!!!********")
    print("Média de escanteios em casa:", mediaEscanteiosCasa)
    print("Média de escanteios para o outro time em casa:", mediaEscanteiosSofridosCasa)
    print("\n********Cálculo de médias de escanteios fora!!!********")
    print("Média de escanteios fora:", mediaEscanteiosFora)
    print("Média de escanteios para o outro time fora:", mediaEscanteiosSofridosFora)
    print("\n********Cálculo de médias totais de escanteios!!!********")
    print("Média de escanteios totais:", mediaEscanteiosTotal)
    print("Média de escanteios para o outro time totais:", mediaEscanteiosSofridosTotal)

    with open('Analise.txt', 'a', encoding="utf-8") as arquivo:
        print("\n********Cálculo de médias de escanteios em casa!!!********", file=arquivo)
        print("Média de escanteios em casa:", mediaEscanteiosCasa, file=arquivo)
        print("Média de escanteios para o outro time em casa:", mediaEscanteiosSofridosCasa, file=arquivo)
        print("\n********Cálculo de médias de escanteios fora!!!********", file=arquivo)
        print("Média de escanteios fora:", mediaEscanteiosFora, file=arquivo)
        print("Média de escanteios para o outro time fora:", mediaEscanteiosSofridosFora, file=arquivo)
        print("\n********Cálculo de médias totais de escanteios!!!********", file=arquivo)
        print("Média de escanteios totais:", mediaEscanteiosTotal, file=arquivo)
        print("Média de escanteios para o outro time totais:", mediaEscanteiosSofridosTotal , "\n\n\n", file=arquivo)
    arquivo.close();