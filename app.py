from fastapi import FastAPI
from pydantic import BaseModel

app = FastAPI()

class Query(BaseModel):
    input: str

@app.post("/agent1")
def generate_blog(query: Query):

    topic = query.input

    output = topic

    return {"output": output}
