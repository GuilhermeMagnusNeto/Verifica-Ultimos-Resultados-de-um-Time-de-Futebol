def calcularMediaPosseDeBola(timePesquisado):
    #armazena informações do arquivo na variavel partidas
    with open('dados.txt', 'r', encoding="utf-8") as arq:
        partidas = arq.readlines()
        for i in range(len(partidas)):
            partidas[i]=partidas[i].replace("\n", "")
    arq.close();

    #variáveis das média
    mediaPosseCasa = 0
    mediaPosseFora = 0
    mediaPosseTotal = 0
    mediaPosseSofridosCasa = 0
    mediaPosseSofridosFora = 0
    mediaPosseSofridosTotal = 0
    #variáveis total de Posse feitos
    totalPosseCasa = 0
    totalPosseFora = 0
    totalPosse = 0
    #variáveis total de Posse sofridos
    totalPosseSofridosCasa = 0
    totalPosseSofridosFora = 0
    totalPosseSofridos = 0
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
                totalPosseCasa = totalPosseCasa+float(partidas[contador+13])
                totalPosseSofridosCasa = totalPosseSofridosCasa+float(partidas[contador+14])
                quantidadeJogosCasa = quantidadeJogosCasa+1
            else:
                totalPosseFora = totalPosseFora+float(partidas[contador+14])
                totalPosseSofridosFora = totalPosseSofridosFora+float(partidas[contador+13])
                quantidadeJogosFora = quantidadeJogosFora+1

    #calculo dos total de Posse
    totalPosse = totalPosseFora + totalPosseCasa
    totalPosseSofridos = totalPosseSofridosFora + totalPosseSofridosCasa
    quantidadeJogosTotal = quantidadeJogosFora+quantidadeJogosCasa
    #calculo da media de Posse feitos
    mediaPosseCasa = totalPosseCasa/quantidadeJogosCasa
    mediaPosseFora = totalPosseFora/quantidadeJogosFora
    mediaPosseTotal = totalPosse/quantidadeJogosTotal
    #calculo da media de Posse sofridos
    mediaPosseSofridosCasa = totalPosseSofridosCasa/quantidadeJogosCasa
    mediaPosseSofridosFora = totalPosseSofridosFora/quantidadeJogosFora
    mediaPosseSofridosTotal = totalPosseSofridos/quantidadeJogosTotal

    print("\n********Cálculo de média de posse em casa!!!********")
    print("Média de posse em casa:", mediaPosseCasa)
    print("Média de Posse sofridos em casa:", mediaPosseSofridosCasa)
    print("\n********Cálculo de média de posse fora!!!********")
    print("Média de posse fora:", mediaPosseFora)
    print("Média de posse sofridos fora:", mediaPosseSofridosFora)
    print("\n********Cálculo de média total de posse!!!********")
    print("Média de posse total:", mediaPosseTotal)
    print("Média de posse sofridos total:", mediaPosseSofridosTotal)

    with open('Analise.txt', 'a', encoding="utf-8") as arquivo:
        print("\n********Cálculo de média de posse em casa!!!********", file=arquivo)
        print("Média de posse feitos em casa:", mediaPosseCasa,file=arquivo)
        print("Média de posse sofridos em casa:", mediaPosseSofridosCasa,file=arquivo)
        print("\n********Cálculo de média de posse fora!!!********",file=arquivo)
        print("Média de posse feitos fora:", mediaPosseFora,file=arquivo)
        print("Média de posse sofridos fora:", mediaPosseSofridosFora,file=arquivo)
        print("\n********Cálculo de média total de posse!!!********",file=arquivo)
        print("Média de posse feitos total:", mediaPosseTotal,file=arquivo)
        print("Média de posse sofridos total:", mediaPosseSofridosTotal,"\n\n\n",file=arquivo)
    arquivo.close();
