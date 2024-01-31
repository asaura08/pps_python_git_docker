from email.policy import default
from urllib import response
from fastapi import FastAPI, Request, Response
from fastapi.responses import HTMLResponse

app = FastAPI()

# Ruta de la página principal
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