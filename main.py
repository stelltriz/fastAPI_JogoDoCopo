from fastapi import FastAPI, HTTPException, status
from fastapi.middleware.cors import CORSMiddleware

import random
from models import Chute

app = FastAPI()

# Configuração do CORS
app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],  # Permitir todas as origens, você pode restringir a origem desejada
    allow_credentials=True,
    allow_methods=["GET", "POST", "OPTIONS"],  # Permitir métodos GET, POST e OPTIONS
    allow_headers=["*"],  # Permitir todos os cabeçalhos, você pode restringir os cabeçalhos desejados
)

copos = [0, 0, 1]

@app.post("/embaralhar")
async def embaralhar_copos():
    random.shuffle(copos)
    return {"message": ""}

@app.get("/resposta")
async def get_resposta():
    for i, cup in enumerate(copos):
        if cup == 1:
            return {"resposta": i}
    raise HTTPException(
        status_code=status.HTTP_500_INTERNAL_SERVER_ERROR, detail="Resposta não encontrada"
    )

@app.post("/chute")
async def post_chute(chute: Chute):
    if chute.copo == copos.index(1):
        return {"message": "Você acertou!", "confetti": True}
    else:
        return {"message": "Você errou!", "confetti": False}

if __name__ == "__main__":
    import uvicorn
    uvicorn.run("main:app", host="127.0.0.1", port=8000, reload=True)
