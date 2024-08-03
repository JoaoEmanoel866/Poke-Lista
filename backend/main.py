from fastapi import FastAPI
from pydantic import BaseModel
import requests
import random



app = FastAPI()

class Produto(BaseModel):
    nome: str

lista_produto = ["coca", "cerveja", "bolo", "linguiça"]

@app.get("/")
def saudacao():
    return 'Hello World'


@app.get("/listar-pokemons")
def listar_pokemons():
    # Gerar um numero aleatório de 1 a 5
    quantidade_pokemons = random.randint(1, 10)
    id_pokemon = str(random.randint(1, 100))
    # fazer a requisição para API do Pokemon para listar a quantidade aleatória de pokemons
    
    lista_pokemons = []
    
    for i in range(0, quantidade_pokemons):
        id_pokemon = str(random.randint(1, 100))
        resposta = requests.get(("https://pokeapi.co/api/v2/pokemon/"+id_pokemon))
        
        nome_pokemon = resposta.json()['name']
        
        numero_pokemon = resposta.json()['id']
        
        imagem_pokemon = resposta.json()['sprites']['other']['official-artwork']['front_default']
        
        lista_pokemons.append({
            'id': numero_pokemon,
            'nome': nome_pokemon,
            'img': imagem_pokemon
        })
        
        
    
    
    #if resposta.status_code == 200:
        #return resposta.json()
    # retorna o resultado dessa requisição no return
    return lista_pokemons

    