from fastapi import FastAPI
from fastapi.responses import RedirectResponse
from fastapi.staticfiles import StaticFiles

app = FastAPI()

from backend.route.user import router as user_router  # Importando as rotas de 'user.py'

# Montando a pasta 'frontend' para servir arquivos estáticos
app.mount("/frontend", StaticFiles(directory="frontend"), name="frontend")

# Incluindo rotas
app.include_router(user_router, prefix="/user", tags=["User"])

@app.get("/")
def redirect_to_frontend():
    # Redirecionando para o arquivo HTML principal na pasta frontend
    return RedirectResponse(url="/frontend/index.html")

# Função de teste para entendimento da API
@app.get("/mensagem")
def saudation():
    return {"mensagem":"Hello World"}