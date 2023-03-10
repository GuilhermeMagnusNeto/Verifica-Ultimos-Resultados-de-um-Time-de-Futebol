def lerDados():
    with open('dados.txt', 'r', encoding="utf-8") as arq:
        partidas = arq.readlines()
        for i in range(len(partidas)):
            partidas[i]=partidas[i].replace("\n", "")
        for item in partidas:
            print(item)
    arq.close();