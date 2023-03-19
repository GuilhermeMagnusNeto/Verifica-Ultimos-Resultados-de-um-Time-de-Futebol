import Escanteios.pegarIdPartidas as pegarId
import Escanteios.raspagemEscanteios as raspagemEscanteios
import Escanteios.criaArquivo as arquivo
import Escanteios.pegaValorCartoes as valorCartoes
import Escanteios.pegarValorEscanteio as valorEscanteios

#efetua leitura do arquivo e pega id das partidas
idPartidas = pegarId.pegarIdPartidas()

#Faz a raspagem de dados e pega os valores dos escanteios e cartões
escanteios, cartoes = raspagemEscanteios.raspagemEscanteios(idPartidas)

print("Escanteios:", escanteios)
print("Cartões:" , cartoes)
