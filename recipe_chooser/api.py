import uvicorn
from fastapi import FastAPI, Path, HTTPException, status

import crud
import exception_msgs
from endpoints import RECIPES, RECIPE_BY_ID

app = FastAPI()


@app.get('/')
def home():
    return 'It works!'


@app.post(RECIPES)
def create_recipe():
    pass


@app.put(RECIPE_BY_ID)
def edit_recipe():
    pass


@app.delete(RECIPE_BY_ID)
def delete_recipe():
    pass


@app.get(RECIPE_BY_ID, status_code=status.HTTP_200_OK)
def get_recipe_by_id(recipe_id: int = Path(None)):
    item = crud.get_recipe_by_id(recipe_id)
    if not item:
        raise HTTPException(status_code=404, detail=exception_msgs.ITEM_NOT_FOUND)
    return item


@app.get(RECIPES)
def get_all_recipes(ingredient: str = None, random: bool = False):
    # if not random then use page and offset
    if ingredient:
        return f'Recipes by {ingredient}'
    return 'All recipes'


if __name__ == '__main__':
    uvicorn.run("api:app", host='0.0.0.0', port=8000, log_level='info', reload=True)


