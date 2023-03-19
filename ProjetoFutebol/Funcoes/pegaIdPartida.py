def idPartida(lista):
    idPartidas = []
    for linhas in range (len(lista)):
        if ('[{"id"' in lista[linhas] and '"sportId"' in lista[linhas+2]) or ('{"id"' in lista[linhas] and '"sportId"' in lista[linhas+2]):
            idPartidas.append(lista[linhas+1])
    return idPartidas