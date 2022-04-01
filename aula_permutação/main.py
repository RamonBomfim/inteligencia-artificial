import random as r
from algoritmo_genético import AlgoritmoGenetico

letras = ['A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N']


def criarIndividuo(letras):
    copia = letras[:]

    r.shuffle(copia)

    return copia


def funFitness(genes, letras):
    dados = 0

    for i in range(len(genes)):
        if(genes[i] == letras[i]):
            dados += 1

    return dados


def mutacao(genes):
    pos1 = r.randint(0, len(genes) - 1)
    pos2 = r.randint(0, len(genes) - 1)

    x = genes[pos1]
    y = genes[pos2]
    genes[pos1] = y
    genes[pos2] = x

    return genes


def crossover(pai1, pai2):
    indiceAleatorio = r.randint(0, len(pai1) - 1)

    # Pega os primeiros do pai 1
    genes1_1 = pai1[:indiceAleatorio]
    # Recupera na ordem os próximos do pai 2
    genes1_2 = []

    for letra in pai2:
        if(letra not in genes1_1):
            genes1_2.append(letra)

    # Pega os primeiros do pai 2
    genes2_1 = pai2[:indiceAleatorio]
    # Recupera na ordem os próximos do pai 1
    genes2_2 = []

    for letra in pai1:
        if(letra not in genes2_1):
            genes2_2.append(letra)

    genes1 = genes1_1 + genes1_2
    genes2 = genes2_1 + genes2_2

    return genes1, genes2


ag = AlgoritmoGenetico(letras, tamPopulacao=10, limGeracoes=500, funcaoFitness=funFitness)
ag.funCriaIndividuo = criarIndividuo
ag.funCrossover = crossover
ag.funMutacao = mutacao
ag.executa()
print(ag.melhorResultado())
