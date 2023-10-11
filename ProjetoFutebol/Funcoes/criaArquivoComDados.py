def criaArquivo(listaTimes):
    contador=0;
    quantidadeJogos = input("Quantos jogos você deseja utilizar para calcular as médias?\n")

    with open('dados.txt', 'w', encoding="utf-8") as arquivo:
        for item in listaTimes:
            if (contador==(15*int(quantidadeJogos))):
                break
            elif (contador==0):
                print(item, file=arquivo)
            elif (contador%15 == 0):
                print(("\n")+item, file=arquivo)
            else:
                print(item, file=arquivo)
            contador=contador+1
    arquivo.close();
