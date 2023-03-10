import uvicorn
from fastapi import FastAPI

from api.routers import measures, ingredients
from config import settings

app = FastAPI()

app.include_router(measures.router)
app.include_router(ingredients.router)


@app.get('/', tags=['Home'])
def home():
    return 'It works!'


if __name__ == '__main__':
    uvicorn.run("app:app", host=settings.api_host, port=settings.api_port, log_level=settings.log_level, reload=True)
