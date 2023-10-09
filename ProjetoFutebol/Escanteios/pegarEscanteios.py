def valorEscanteiosCartoes(idPartidas): 
    import requests
    import re

    #Faz a raspagem de dados e pega os valores dos escanteios e cartões
    contador = 0
    escanteios = []
    cartoes = []
    while(contador < len(idPartidas)):
        url = "https://webws.365scores.com/web/game"

        querystring = {"appTypeId":"5","langId":"31","timezoneName":"America/Sao_Paulo","userCountryId":"21","gameId":idPartidas[contador],"matchupId":"9080-10270-418"}

        payload = ""
        response = requests.request("GET", url, data=payload, params=querystring)
        lista = []
        lista = re.split('[,:=&]', response.text)

        #DEVO PEGAR AS DEMAIS INFORMAÇÕES AQUII

        #pega o valor dos escanteios
        for item in range(len(lista)):
            if '"Escanteios"' == lista[item]:
                escanteios.append(lista[item+8])

        #pega o valor dos cartões
        for item in range(len(lista)):
            if '"Cartões amarelos"' == lista[item]:
                cartoes.append(lista[item+8])
        contador = contador + 1

    return  escanteios, cartoes
