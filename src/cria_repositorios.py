import requests
import base64
from dotenv import load_dotenv
import os

load_dotenv()

class CriaRepositorios:
    def __init__(self, username):
        self.username = username
        self.api_base = 'https://api.github.com'
        self.acess_token = os.getenv('GITHUB_TOKEN')
        self.headers = {'Authorization': 'token ' + self.acess_token,
                                  'Accept': 'application/vnd.github+json'}
        
    def cria_repositorio(self, nome_repo):
        print("→ Criando repositório...")
        data = {
            'name': nome_repo,
            'description': 'Repositorio sobre dados de linguagens de empresas criado via API',
            'private': False,   
        }
        response = requests.post(f'{self.api_base}/user/repos', json=data, headers=self.headers)

        print(f'Repositório {nome_repo} criado com status: {response.status_code}')

    def adiciona_arquivo(self, nome_repo, nome_arquivo, path):
        print(f"→ Adicionando {nome_arquivo} ao repositório...")
        with open(path, 'rb') as file:
            file_content = file.read()
        encoded_content = base64.b64encode(file_content).decode('utf-8')

        url = f'{self.api_base}/repos/{self.username}/{nome_repo}/contents/{nome_arquivo}'

        data = {
            'message': f'Adicionando {nome_arquivo} ao repositório {nome_repo}',
            'content': encoded_content
        }

        response = requests.put(url, json=data, headers=self.headers)
        print(f'Arquivo {nome_arquivo} adicionado ao repositório {nome_repo} com status: {response.status_code}')
