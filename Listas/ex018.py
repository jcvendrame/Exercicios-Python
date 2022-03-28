'''
Enquete - Qual o melhor jogador
'''
pVoto = 1
def calcularPVoto(tVoto, vJogador):
    """
    -> Calcula o percentual de voto de cada jogador que recebeu voto
    :param tVoto: Quantidade total de votos computados
    :param vJogador: Quantidade de votos do jagador a ser calculado o percentual
    Função criada por Jcvendrame
    """
    return (vJogador / tVoto) * 100


votos = []
totVotos = 0
while True:
    voto = int(input("Seu voto entre 1 e 23: [0=fim] "))
    if(voto == 0):
        break
    if(voto > 23 or voto < 0):
        print("Voto inválido! ")
    else:
        votos.append(voto)
        totVotos += 1
print(votos)
votos.sort()
print(votos)
print(f"Total de votos computados: {totVotos}")
print("Jogador   Votos   %")
for i in range(1, 23):
    if(votos.count(i) > 0):
        qVotos = votos.count(i)
        pVoto = calcularPVoto(totVotos, qVotos)
        print(f"{i:<10}{qVotos:<7}{pVoto:.2f}")