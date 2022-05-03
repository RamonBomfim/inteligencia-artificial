from sklearn.cluster import KMeans
import pandas as pd

csv = pd.read_csv('dados.csv', sep=',')
csv = csv.drop(columns=['id', 'tipo', 'data_publicacao', 'num_reacoes'])
dados = csv.values

numero_centroides = 3
modelo = KMeans(numero_centroides, random_state=0)
modelo.fit(dados)

print("Informe os dados da postagem para que seja dito o grupo vinculado:")
num_comentarios = int(input("Número de comentários: "))
num_compartilhamentos = int(input("Número de compartilhamentos: "))
num_likes = int(input("Número de Likes: "))
num_loves = int(input("Número de Loves: "))
num_wows = int(input("Número de Wows: "))
num_hahas = int(input("Número de Risos: "))
num_sads = int(input("Número de Carinhas tristes: "))
num_angrys = int(input("Número de Raiva: "))

resultado = modelo.predict([[num_comentarios, num_compartilhamentos,
                           num_likes, num_loves, num_wows, num_hahas, num_sads, num_angrys]])

print(f"Grupo: {resultado[0]}")
