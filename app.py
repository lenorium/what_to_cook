import uvicorn
from fastapi import FastAPI

from api.routers import measures, recipes

app = FastAPI()

# app.include_router(recipes.router)
app.include_router(measures.router)


@app.get('/', tags=['Home'])
def home():
    return 'It works!'

# @app.on_event('startup'):


if __name__ == '__main__':
    uvicorn.run("app:app", host='0.0.0.0', port=8000, log_level='info', reload=True)


