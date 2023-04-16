import uvicorn
from fastapi import FastAPI

app = FastAPI()


@app.get('/')
def fist_api() -> str:
    return 'This API it´s run!'



if __name__ == "__main__":
    uvicorn.run(app, port=8001)