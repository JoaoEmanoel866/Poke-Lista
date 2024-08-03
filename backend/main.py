from fastapi import FastAPI
from pydantic import BaseModel
import requests
import random



app = FastAPI()

class Produto(BaseModel):
    nome: str

lista_pokemons = []
pokemon_capturado = []

@app.get("/")
def saudacao():
    return 'Hello World'


@app.get("/listar-pokemons")
def listar_pokemons():
    quantidade_pokemons = random.randint(1, 10)
    id_pokemon = str(random.randint(1, 100))
    
    
    
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
        
        
    
    
    return lista_pokemons

@app.get("/capturar-pokemon/{nome_pokemon}")
def capturar_pokemon(nome_pokemon):
    chance_captura = random.randint(1, 100)
       
    if chance_captura < 70:
        

        for i in lista_pokemons:

            if i['nome'] == nome_pokemon:
                
                pokemon_capturado.append(i)
                
        return "Voce capturou " + nome_pokemon + " com sucesso"
    
    else:
        return "A captura falhou"
    
    
    
@app.get("/pokemons-capturados")
def lista_capturados():
    
    return pokemon_capturado