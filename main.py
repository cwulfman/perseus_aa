from fastapi import FastAPI
from typing import Union
from app.routers import artifacts

app = FastAPI()

app.include_router(artifacts.router)

@app.get('/')
async def read_root():
    return { "message": "Hello" }
