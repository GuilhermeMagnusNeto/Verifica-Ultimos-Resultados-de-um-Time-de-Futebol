#armazena informações do arquivo na variavel partidas
with open('dados.txt', 'r', encoding="utf-8") as arq:
    partidas = arq.readlines()
    for i in range(len(partidas)):
        partidas[i]=partidas[i].replace("\n", "")
arq.close();

#variáveis
mediaGolsCasa = 0
mediaGolsFora = 0
mediaGolsTotal = 0

# descobrindo o nome do time que foi pesquisado
if 0 == 0:
    timePesquisado = partidas[0]
elif 1 == 1:
    timePesquisado = partidas[4]

print(timePesquisado)
# for contador in range(len(partidas)):
#     if partidas[contador] == "Gr":

