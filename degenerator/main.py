from fastapi import FastAPI
from degenerator.model import TextDegenerator

app = FastAPI()

model = TextDegenerator()


@app.get("/")
async def root():
    return {"message": "Hello World"}


@app.get("/new")
def get_text():
    return {"text": model.generate()}
