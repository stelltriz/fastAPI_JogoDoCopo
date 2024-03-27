from fastapi import FastAPI, HTTPException, status
import random
from models import Chute

app = FastAPI()

copos = [0, 0, 1]
random.shuffle(copos)

if copos[0] == 1:
    resposta = 0

elif copos[1] == 1:
    resposta = 1

elif copos[2] == 1:
    resposta = 2


@app.get("/resposta")
async def get_resposta():
    return resposta


@app.post("/chute")
async def post_chute(chute: Chute):
    if chute.copo == resposta:
        print("Você Acertou!")
    elif chute.copo <= 3 and chute.copo >= 0 and chute.copo != resposta:
        print("Você errou!")
    else:
        raise HTTPException(
            status_code=status.HTTP_404_NOT_FOUND, detail="Número Inválido"
        )


if __name__ == "__main__":  # variável que o python cria sempre no arquivo principal
    import uvicorn

    uvicorn.run("main:app", host="127.0.0.1", port=8000, reload=True)
