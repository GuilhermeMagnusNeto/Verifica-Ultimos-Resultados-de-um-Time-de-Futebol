import pegarValorEscanteio as pegarEscanteio
import pegaValorCartoes as pegarCartoes
import requests
import re

def raspagemEscanteios(idPartidas):
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

        escanteios.append(pegarEscanteio.pegarValorEscanteio(lista))
        cartoes.append(pegarCartoes.pegarValorCartoes(lista))
        contador = contador + 1
    return escanteios, cartoes