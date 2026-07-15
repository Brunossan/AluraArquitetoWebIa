# Importa a classe FastAPI do módulo fastapi
from fastapi import FastAPI

# Cria uma instância do aplicativo FastAPI
app = FastAPI()

# Define uma rota para o método HTTP GET no caminho raiz "/"
@app.get("/")
def hello_world():
    # Retorna um dicionário que o FastAPI converterá automaticamente em JSON
    return {"mensagem": "Olá, mundo! 🌍"}
