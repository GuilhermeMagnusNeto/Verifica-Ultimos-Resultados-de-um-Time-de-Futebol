def pegarIdPartidas():
    with open('dados.txt', 'r', encoding="utf-8") as arq:
        partidas = arq.readlines()
        for i in range(len(partidas)):
            partidas[i]=partidas[i].replace("\n", "")
    arq.close();

    idPartidas = []
    for linha in range(len(partidas)):
        if linha == 0:
            idPartidas.append(int(partidas[linha]))
        elif linha%7 == 0:
            idPartidas.append(int(partidas[linha]))
    return idPartidas