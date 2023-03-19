import Funcoes.raspagemDadosTime as raspagem
import Funcoes.pegaIdTimePesquisado as pegarId
import Funcoes.criaListaJogos as listaJogos
import Funcoes.criaListaTimes as listaTimes
import Funcoes.criaArquivoComDados as arquivo
import Funcoes.leituraDados as lerDados
import Funcoes.calcularMediaGols as calcularMedia
import Funcoes.descobrirTimePesquisado as descobrirTime
import Funcoes.pegaIdPartida as pegarIdPartida
import re

print("\n1 - Efetuar raspagem de dados!\n")
print("2 - Efetuar leitura dos dados!\n")
print("3 - Calcular média de gols!\n")
print("4 - Calcular média de escanteios!\n")
print("6 - Sair!\n\n")
escolha = input("Escolha a opção desejada: ")
while (escolha!="6"):
    match escolha:
        case "1":
            #faz a raspagem de dados do arquivo da pagina
            response = raspagem.raspagemDados()

            #cria uma lista dessa raspagem de dados
            lista = []
            lista = re.split('[,:=&]', response.text)
            
            #pega o Id da partida
            idPartidas = pegarIdPartida.idPartida(lista)
            #pega o ID do time que foi pesquisado
            idTimePesquisado = pegarId.pegarIdTimePesquisado(lista)

            #descobre o time pesquisado
            timePesquisado = descobrirTime.descobreTimePesquisado(lista, idTimePesquisado)

            #separa dados e deixa apenas informações do time da casa e de fora
            listaJogos = listaJogos.criaListaJogos(lista)
            #pega o resultado dos ultimos jogos com o nome dos times e placar
            listaTimes = listaTimes.criaListaTimes(listaJogos, idPartidas)
            #coloca as informações dentro de um txt
            arquivo.criaArquivo(listaTimes)
            print("Processo concluido!!!\n")

        case "2":
            lerDados.lerDados()
        case "3":
            calcularMedia.calcularMediaGols(timePesquisado)
        case "4":
            pegarEscanteios.pegaEscanteios()
        case "6":
            break;
        case _:
            print("Valor inválido, por favor tente novamente!!!\n")
    
    print("\n1 - Efetuar raspagem de dados!\n")
    print("2 - Efetuar leitura dos dados!\n")
    print("3 - Calcular média de gols!\n")
    print("4 - Calcular média de escanteios!\n")
    print("6 - Sair!\n\n")
    escolha = input("Escolha a opção desejada: ");