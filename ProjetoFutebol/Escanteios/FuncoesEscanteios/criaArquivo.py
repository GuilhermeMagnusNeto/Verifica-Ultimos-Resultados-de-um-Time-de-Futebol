def criaArquivo(listaTimes):
    contador=0;

    with open('escanteios.txt', 'w', encoding="utf-8") as arquivo:
        for item in listaTimes:
            if (contador==0):
                print(item, file=arquivo)
            elif (contador%6 == 0):
                print(("\n")+item, file=arquivo)
            else:
                print(item, file=arquivo)
            contador=contador+1
    arquivo.close();