from fastapi import FastAPI
from fastapi.staticfiles import StaticFiles
import os

# 1. Cria a instância do aplicativo FastAPI
app = FastAPI()

# 2. Define os caminhos absolutos da pasta base e da pasta de imagens (imgs)
# Isso garante que a pasta seja encontrada independentemente de onde o script seja executado
PASTA_BASE = os.path.dirname(os.path.abspath(__file__))
PASTA_IMAGENS = os.path.join(PASTA_BASE, "imgs")

# Garante que a pasta de imagens exista
os.makedirs(PASTA_IMAGENS, exist_ok=True)

# 3. Configura o FastAPI para servir arquivos estáticos
# Mapeia a pasta física PASTA_IMAGENS para a rota "/imgs"
app.mount("/imgs", StaticFiles(directory=PASTA_IMAGENS), name="imgs")

# 4. Define a lista de figurinhas contendo os químicos famosos e suas respectivas imagens
figurinhas = [
    {
        "id": 1,
        "nome": "Antoine Lavoisier",
        "categoria": "Química",
        "imagem_url": "/imgs/01-antoine-lavoisier.png"
    },
    {
        "id": 6,
        "nome": "Marie Curie",
        "categoria": "Química",
        "imagem_url": "/imgs/06-marie-curie.png"
    },
    {
        "id": 11,
        "nome": "Dmitri Mendeleev",
        "categoria": "Química",
        "imagem_url": "/imgs/11-dmitri-mendeleev.png"
    },
    {
        "id": 16,
        "nome": "John Dalton",
        "categoria": "Química",
        "imagem_url": "/imgs/16-john-dalton.png"
    },
    {
        "id": 21,
        "nome": "Linus Pauling",
        "categoria": "Química",
        "imagem_url": "/imgs/21-linus-pauling.png"
    },
    {
        "id": 26,
        "nome": "Louis Pasteur",
        "categoria": "Química",
        "imagem_url": "/imgs/26-louis-pasteur.png"
    }
]

# 5. Define o único endpoint GET "/figurinhas" que retorna a lista de figurinhas
@app.get("/figurinhas")
def listar_figurinhas():
    """
    Retorna a lista completa das figurinhas disponíveis no servidor.
    """
    return figurinhas

