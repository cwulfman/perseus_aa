from fastapi import FastAPI
from typing import Union


app = FastAPI()

@app.get('/')
def read_root():
    return {"Hello": "World"}


@app.get("/artifacts/{artifact_id}")
def read_artifact(artifact_id: str, q: Union[str, None] = None):
    return {"artifact_id": artifact_id, "q": q}
