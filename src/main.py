from src.dados_repos import DadosRepositorios
from src.cria_repositorios import CriaRepositorios
from src.utils import gera_grafico_pizza
import os
from dotenv import load_dotenv

load_dotenv()

empresas = {
    'facebook': 'dados_facebook.csv',
    'amazon': 'dados_amazon.csv',
    'netflix': 'dados_netflix.csv',
    'spotify': 'dados_spotify.csv',
    'apple': 'dados_apple.csv',
    'github': 'dados_github.csv',
    'airbnb': 'dados_airbnb.csv'
}

print("\n Iniciando coleta de dados das empresas...")
for usuario_github, nome_arquivo in empresas.items():
    print(f"\nColetando dados de {usuario_github}...")
    extrator = DadosRepositorios(usuario_github)
    df = extrator.cria_df_de_linguagens()
    
    caminho_csv = os.path.join('data', nome_arquivo)
    df.to_csv(caminho_csv, index=False)
    print(f"Dados salvos em: {caminho_csv}")

    gera_grafico_pizza(df, usuario_github)

usuario = 'duffess'
repositorio_nome = 'linguagens_utilizadas_empresas2'

print(f"\nCriando repositório: {repositorio_nome}")
uploader = CriaRepositorios(usuario)
uploader.cria_repositorio(repositorio_nome)

print("\nEnviando arquivos...")
for _, nome_arquivo in empresas.items():
    caminho = os.path.join('data', nome_arquivo)
    uploader.adiciona_arquivo(repositorio_nome, nome_arquivo, caminho)

print(f"\nProjeto finalizado! Repositório `{repositorio_nome}` criado e arquivos enviados.")

