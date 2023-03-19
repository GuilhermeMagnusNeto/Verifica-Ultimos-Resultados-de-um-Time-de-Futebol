import requests
import re
import FuncoesEscanteios.criaArquivo as arquivo
import FuncoesEscanteios.pegarValorEscanteio as pegarEscanteio
import FuncoesEscanteios.pegaValorCartoes as pegarCartoes

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

print("Escanteios:", escanteios)
print("Cartões:" , cartoes)
