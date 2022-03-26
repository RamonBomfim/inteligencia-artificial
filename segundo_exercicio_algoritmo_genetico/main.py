from operator import index
import random
from algoritmo_genético import AlgoritmoGenetico

dados = ['x', 'y', 'z']


def criarIndividuo(dados):
    genes = []

    for i in range(len(dados)):
        genes.append(random.randint(0, 50))

    return genes


def funFitness(genes, dados):
    valor_final = 0
    x = genes[0]
    y = genes[1]
    z = genes[2]

    valor_final += abs((5 * x + 3 * y - z) - 39)

    return valor_final


def mutacao(genes):
    index_aleatorio = random.randint(0, len(genes) - 1)
    genes[index_aleatorio] = random.randint(0, 50)

    return genes


ag = AlgoritmoGenetico(
    dados,
    tamPopulacao=20,
    limGeracoes=1000,
    probMutacao=5,
    funcaoFitness=funFitness,
    maiorFitness=False
)

ag.funCriaIndividuo = criarIndividuo
ag.funMutacao = mutacao
ag.executa()

print(ag.melhorResultado())
