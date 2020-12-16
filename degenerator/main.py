from fastapi import FastAPI
from fastapi.responses import FileResponse

from degenerator.bless_rng import (
    get_random_pic,
    get_random_style_transfer,
    get_random_style_transfer_url,
)
from degenerator.model import TextDegenerator

app = FastAPI()

model = TextDegenerator()


@app.get("/")
async def root():
    return {"message": "Hello World"}


@app.get("/text")
def get_text():
    return {"text": model.generate()}


@app.get("/pic")
def get_pic():
    with open("temp_img.jpg", "wb") as file:
        file.write(get_random_pic())
    return FileResponse("temp_img.jpg")


@app.get("/style")
def get_style():
    with open("random_style.jpg", "wb") as file:
        file.write(get_random_style_transfer())
    return FileResponse("random_style.jpg")


@app.get("/style_url")
def get_style_url():
    return get_random_style_transfer_url()
