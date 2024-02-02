from typing import Annotated
from unittest import result
from fastapi import FastAPI, Request, Body
from fastapi.responses import HTMLResponse, JSONResponse
from pydantic import Json, BaseModel
from bayeta import frotar, frotar_insertar

app = FastAPI()

class Frase(BaseModel):
    frase: str


@app.get("/", response_class=HTMLResponse)
async def read_root(request: Request):
    html_content = """
    <html>
    <head>
        <style>
            body {
                display: flex;
                justify-content: center;
                align-items: center;
                height: 100vh;
                margin: 0;
                font-size: 2rem;
            }
        </style>
    </head>
    <body>
        <h1>Hola mundo</h1>
    </body>
    </html>
    """
    return html_content

@app.get("/frotar/{n_frases}", response_class=JSONResponse)
async def read_frotar(request: Request, n_frases: int):
    return frotar(n_frases)

@app.get("/frotar", response_class=JSONResponse)
async def read_frotar(request: Request):
    return frotar(1)

@app.post("/frotar/add", response_class=JSONResponse)
async def read_frotar_add(frases: Annotated[Frase, Body(
    examples=[{
        "frase": "Frase de ejemplo"
    }]
)]):
    frotar_insertar(frases)
    return JSONResponse(status_code=200, content={"message": "Frases añadidas"})