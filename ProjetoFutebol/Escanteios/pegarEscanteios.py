import FuncoesEscanteios.pegarIdPartidas as pegarId
import FuncoesEscanteios.raspagemEscanteios as raspagemEscanteios

def pegaEscanteios():
    #efetua leitura do arquivo e pega id das partidas
    idPartidas = pegarId.pegarIdPartidas()

    #Faz a raspagem de dados e pega os valores dos escanteios e cartões
    escanteios, cartoes = raspagemEscanteios.raspagemEscanteios(idPartidas)

    print("Escanteios:", escanteios)
    print("Cartões:" , cartoes)
