import matplotlib.pyplot as plt
import os

def gera_grafico_pizza(df, nome_empresa):
    df_clean = df['language'].dropna()
    contagem = df_clean.value_counts()
    plt.figure(figsize=(8, 8))
    contagem.plot.pie(autopct='%1.1f%%', startangle=140, shadow=True)
    plt.title(f'Linguagens usadas por {nome_empresa.capitalize()}')
    plt.ylabel('')  # remove label do eixo y

    caminho_imagem = os.path.join('images', f'grafico_pizza_{nome_empresa}.png')
    plt.savefig(caminho_imagem)
    plt.close()
    print(f'Gráfico salvo em: {caminho_imagem}')
