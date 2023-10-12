def calcularMediaGols(timePesquisado):
    #armazena informações do arquivo na variavel partidas
    with open('dados.txt', 'r', encoding="utf-8") as arq:
        partidas = arq.readlines()
        for i in range(len(partidas)):
            partidas[i]=partidas[i].replace("\n", "")
    arq.close();

    #variáveis das médias
    mediaGolsCasa = 0
    mediaGolsFora = 0
    mediaGolsTotal = 0
    mediaGolsSofridosCasa = 0
    mediaGolsSofridosFora = 0
    mediaGolsSofridosTotal = 0
    #variáveis total de gols feitos
    totalGolsCasa = 0
    totalGolsFora = 0
    totalGols = 0
    #variáveis total de gols sofridos
    totalGolsSofridosCasa = 0
    totalGolsSofridosFora = 0
    totalGolsSofridos = 0
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
        if contador%16 == 0:
            if partidas[contador+1] == nomeTimePesquisado:
                totalGolsCasa = totalGolsCasa+float(partidas[contador+2])
                totalGolsSofridosCasa = totalGolsSofridosCasa+float(partidas[contador+4])
                quantidadeJogosCasa = quantidadeJogosCasa+1
            else:
                totalGolsFora = totalGolsFora+float(partidas[contador+4])
                totalGolsSofridosFora = totalGolsSofridosFora+float(partidas[contador+2])
                quantidadeJogosFora = quantidadeJogosFora+1

    #calculo dos totais de gols
    totalGols = totalGolsFora + totalGolsCasa
    totalGolsSofridos = totalGolsSofridosFora + totalGolsSofridosCasa
    quantidadeJogosTotal = quantidadeJogosFora+quantidadeJogosCasa
    #calculo da media de gols feitos
    mediaGolsCasa = totalGolsCasa/quantidadeJogosCasa
    mediaGolsFora = totalGolsFora/quantidadeJogosFora
    mediaGolsTotal = totalGols/quantidadeJogosTotal
    #calculo da media de gols sofridos
    mediaGolsSofridosCasa = totalGolsSofridosCasa/quantidadeJogosCasa
    mediaGolsSofridosFora = totalGolsSofridosFora/quantidadeJogosFora
    mediaGolsSofridosTotal = totalGolsSofridos/quantidadeJogosTotal

    print("\n********Cálculo de médias de gols em casa!!!********")
    print("Média de gols feitos em casa:", mediaGolsCasa)
    print("Média de gols sofridos em casa:", mediaGolsSofridosCasa)
    print("\n********Cálculo de médias de gols fora!!!********")
    print("Média de gols feitos fora:", mediaGolsFora)
    print("Média de gols sofridos fora:", mediaGolsSofridosFora)
    print("\n********Cálculo de médias totais de gols!!!********")
    print("Média de gols feitos totais:", mediaGolsTotal)
    print("Média de gols sofridos totais:", mediaGolsSofridosTotal)

    with open('Analise.txt', 'a', encoding="utf-8") as arquivo:
        print("\n********Cálculo de médias de gols em casa!!!********", file=arquivo)
        print("Média de gols feitos em casa:", mediaGolsCasa,file=arquivo)
        print("Média de gols sofridos em casa:", mediaGolsSofridosCasa,file=arquivo)
        print("\n********Cálculo de médias de gols fora!!!********",file=arquivo)
        print("Média de gols feitos fora:", mediaGolsFora,file=arquivo)
        print("Média de gols sofridos fora:", mediaGolsSofridosFora,file=arquivo)
        print("\n********Cálculo de médias totais de gols!!!********",file=arquivo)
        print("Média de gols feitos totais:", mediaGolsTotal,file=arquivo)
        print("Média de gols sofridos totais:", mediaGolsSofridosTotal,"\n\n\n",file=arquivo)
    arquivo.close();
