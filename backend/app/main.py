from fastapi import FastAPI

app = FastAPI()

@app.get("/", status_code=200)
async def hello():
    return {"msg": "Hello World"}