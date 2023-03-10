import Funcoes.raspagemDadosTime as raspagem
import Funcoes.separaElementos as separar
import Funcoes.criaListaJogos as listaJogos
import Funcoes.criaListaTimes as listaTimes
import Funcoes.criaArquivoComDados as arquivo
import Funcoes.leituraDados as lerDados
import re

print("\n1 - Efetuar raspagem de dados!\n")
print("2 - Efetuar leitura dos dados!\n")
print("3 - Sair!\n\n")
escolha = input("Escolha a opção desejada: ");
while (escolha!="3"):
    match escolha:
        case "1":
            #faz a raspagem de dados do arquivo da pagina
            response = raspagem.raspagemDados()

            #cria uma lista dessa raspagem de dados
            lista = []
            lista = re.split('[:,]', response.text)

            #remove parte de games e bookers
            lista = separar.listaJogos(lista)

            #separa dados e deixa apenas informações do time da casa e de fora
            listaJogos = listaJogos.criaListaJogos(lista)
            #pega o resultado dos ultimos jogos com o nome dos times e placar
            listaTimes = listaTimes.criaListaTimes(listaJogos)
            #coloca as informações dentro de um txt
            arquivo.criaArquivo(listaTimes)
            print("Processo concluido!!!\n")
        case "2":
            lerDados.lerDados()
        case "3":
            break;
        case _:
            print("Valor inválido, por favor tente novamente!!!\n")
    
    print("\n1 - Efetuar raspagem de dados!\n")
    print("2 - Efetuar leitura dos dados!\n")
    print("3 - Sair!\n\n")
    escolha = input("Escolha a opção desejada: ");
#TESTE