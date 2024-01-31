from fastapi import FastAPI
from bayeta import frotar

app = FastAPI()

@app.get("/")
async def root():
    return {"message": "Hello World"}