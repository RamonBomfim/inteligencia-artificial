from algoritmo_genético import AlgoritmoGenetico

dados = [
    {"Item": "Item 1", "peso": 4, "valor": 6},
    {"Item": "Item 2", "peso": 3, "valor": 5},
    {"Item": "Item 3", "peso": 2, "valor": 2},
    {"Item": "Item 4", "peso": 8, "valor": 10},
    {"Item": "Item 5", "peso": 4, "valor": 3},
    {"Item": "Item 6", "peso": 12, "valor": 11},
    {"Item": "Item 7", "peso": 5, "valor": 2},
    {"Item": "Item 8", "peso": 13, "valor": 7},
    {"Item": "Item 9", "peso": 3, "valor": 4},
    {"Item": "Item 10", "peso": 9, "valor": 7},
]


def funFitness(genes, dados):
    maior_lucro = 0
    peso_total = 0

    for i in range(len(genes)):
        if genes[i] == 1:
            peso_total += dados[i]['peso']
            maior_lucro += dados[i]['valor']

    if peso_total > 20:
        return 0

    return maior_lucro


ag = AlgoritmoGenetico(
    dados,
    tamPopulacao=100,
    limGeracoes=1000,
    funcaoFitness=funFitness
)

ag.executa()
print(ag.melhorResultado())
