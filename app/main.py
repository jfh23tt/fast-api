from fastapi import FastAPI # type: ignore

app = FastAPI()

@app.get("/")
def leer_root():
    return { "¡Hola mundo desde FastAPI!"}