def calcularMediaCartoes(timePesquisado):
    #armazena informações do arquivo na variavel partidas
    with open('dados.txt', 'r', encoding="utf-8") as arq:
        partidas = arq.readlines()
        for i in range(len(partidas)):
            partidas[i]=partidas[i].replace("\n", "")
    arq.close();

    #variáveis das médias
    mediaCartoesCasa = 0
    mediaCartoesFora = 0
    mediaCartoesTotal = 0
    mediaCartoesSofridosCasa = 0
    mediaCartoesSofridosFora = 0
    mediaCartoesSofridosTotal = 0
    #variáveis total de Cartoes feitos
    totalCartoesCasa = 0
    totalCartoesFora = 0
    totalCartoes = 0
    #variáveis total de Cartoes sofridos
    totalCartoesSofridosCasa = 0
    totalCartoesSofridosFora = 0
    totalCartoesSofridos = 0
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
                totalCartoesCasa = totalCartoesCasa+float(partidas[contador+10])
                totalCartoesSofridosCasa = totalCartoesSofridosCasa+float(partidas[contador+11])
                quantidadeJogosCasa = quantidadeJogosCasa+1
            else:
                totalCartoesFora = totalCartoesFora+float(partidas[contador+11])
                totalCartoesSofridosFora = totalCartoesSofridosFora+float(partidas[contador+10])
                quantidadeJogosFora = quantidadeJogosFora+1

    #calculo dos totais de Cartoes
    totalCartoes = totalCartoesFora + totalCartoesCasa
    totalCartoesSofridos = totalCartoesSofridosFora + totalCartoesSofridosCasa
    quantidadeJogosTotal = quantidadeJogosFora+quantidadeJogosCasa
    #calculo da media de Cartoes feitos
    mediaCartoesCasa = totalCartoesCasa/quantidadeJogosCasa
    mediaCartoesFora = totalCartoesFora/quantidadeJogosFora
    mediaCartoesTotal = totalCartoes/quantidadeJogosTotal
    #calculo da media de Cartoes sofridos
    mediaCartoesSofridosCasa = totalCartoesSofridosCasa/quantidadeJogosCasa
    mediaCartoesSofridosFora = totalCartoesSofridosFora/quantidadeJogosFora
    mediaCartoesSofridosTotal = totalCartoesSofridos/quantidadeJogosTotal

    print("\n********Cálculo de médias de Cartoes em casa!!!********")
    print("Média de cartões tomados em casa:", mediaCartoesCasa)
    print("Média de cartões do outro time em casa:", mediaCartoesSofridosCasa)
    print("\n********Cálculo de médias de Cartoes fora!!!********")
    print("Média de cartões tomados fora:", mediaCartoesFora)
    print("Média de cartões do outro time fora:", mediaCartoesSofridosFora)
    print("\n********Cálculo de médias totais de Cartoes!!!********")
    print("Média de cartões tomados totais:", mediaCartoesTotal)
    print("Média de cartões do outro time totais:", mediaCartoesSofridosTotal)