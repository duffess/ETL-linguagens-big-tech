import requests 
import pandas as pd
from dotenv import load_dotenv
import os

load_dotenv()

class DadosRepositorios:

    def __init__(self, owner):
        self.owner = owner
        self.api_base = 'https://api.github.com'
        self.acess_token = os.getenv('GITHUB_TOKEN')
        self.headers = {'Authorization': 'token ' + self.acess_token,
                                  'Accept': 'application/vnd.github+json'}
        
    def lista_respositorios(self):
        repos_list = []
        page_num = 1

        while True:
            url = f'{self.api_base}/users/{self.owner}/repos?page={page_num}'
            response = requests.get(url, headers=self.headers)
            page_data = response.json()
            if not page_data:
                break
            repos_list.append(page_data)
            page_num += 1
            
        return repos_list
    
    def nome_repositorios(self, repos_list):
        repo_names = []

        for page in repos_list:
            for repo in page:
                try:
                    repo_names.append(repo['name'])
                except:
                    pass

        return repo_names
    
    def nomes_linguagens(self, repos_list):
        repo_languages = []

        for page in repos_list:
            for repo in page:
                try:
                    repo_languages.append(repo['language'])
                except:
                    pass

        return repo_languages
    
    def cria_df_de_linguagens(self):
        repositorios = self.lista_respositorios()
        linguagens = self.nomes_linguagens(repositorios)
        dados = pd.DataFrame()
        dados['language'] = linguagens

        return dados
    