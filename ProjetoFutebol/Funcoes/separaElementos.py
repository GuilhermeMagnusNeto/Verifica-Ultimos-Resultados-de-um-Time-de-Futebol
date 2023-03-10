def listaJogos(lista):
    elemento1 = '"games"'
    elemento2 = '"bookmakers"'
    for linha in range (len(lista)):
        if elemento1 in lista[linha]:
            valorInicio = linha
    del lista[:valorInicio]

    for linha2 in range (len(lista)):
        if elemento2 in lista[linha2]:
            valorFinal = linha2
    del lista[valorFinal:]

    return lista;