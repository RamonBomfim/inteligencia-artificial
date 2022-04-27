import pandas as pd
from sklearn.preprocessing import LabelEncoder
from sklearn.linear_model import LinearRegression

# Lendo dados do arquivo .csv
csv = pd.read_csv('dados.csv', sep=";")

# Normatizando os valores da coluna 'Tipo'
le = LabelEncoder()
csv['Tipo'] = le.fit_transform(csv['Tipo'])

# Criando modelo para Números de comentários
dados_comentario = csv.drop(columns=['like', 'Compartilhamento'])
dados_comentario = dados_comentario.values
atributos1 = dados_comentario[:, :5]
comentarios = dados_comentario[:, 5]

modelo_comentario = LinearRegression()
modelo_comentario.fit(atributos1, comentarios)

# Criando modelo para likes
dados_like = csv.drop(columns=['Número comentários', 'Compartilhamento'])
dados_like = dados_like.values
atributos2 = dados_like[:, :5]
likes = dados_like[:, 5]

modelo_like = LinearRegression()
modelo_like.fit(atributos2, likes)

# Criando modelo para Compartilhamento
dados_compartilhamento = csv.drop(columns=['Número comentários', 'like'])
dados_compartilhamento = dados_compartilhamento.values
atributos3 = dados_compartilhamento[:, :5]
compartilhamentos = dados_compartilhamento[:, 5]

modelo_compartilhamento = LinearRegression()
modelo_compartilhamento.fit(atributos3, compartilhamentos)

# Coletando informações do usuário
tipo = int(input(
    "Informe o número do tipo de postagem: Foto[0] | Link[1] | Status[2] | Vídeo[3]: "))
mes = int(input("Mês da postagem: "))
dia = int(
    input("Dia da postagem: D[1] | S[2] | T[3] | Q[4] | Q[5] | S[6] | S[7]: "))
hora = int(input("Hora da postagem: "))
pago = int(input("Pago: SIM[1] | NÃO[0]: "))

retorno_comentarios = modelo_comentario.predict([[tipo, mes, dia, hora, pago]])
retorno_likes = modelo_like.predict([[tipo, mes, dia, hora, pago]])
retorno_compartilhamentos = modelo_compartilhamento.predict(
    [[tipo, mes, dia, hora, pago]])

print(f"Média de Comentários: {int(retorno_comentarios[0])}")
print(f"Média de Likes: {int(retorno_likes[0])}")
print(f"Média de Compartilhamentos: {int(retorno_compartilhamentos[0])}")
