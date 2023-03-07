from fastapi import APIRouter, HTTPException, Path
from starlette import status

import exceptions
from api.endpoints import RECIPE_BY_ID, RECIPES

router = APIRouter(tags=['Recipes'])


@router.post(RECIPES)
def create_recipe():
    pass


@router.put(RECIPE_BY_ID)
def edit_recipe():
    pass


@router.delete(RECIPE_BY_ID)
def delete_recipe():
    pass


@router.get(RECIPE_BY_ID, status_code=status.HTTP_200_OK)
def get_recipe_by_id(recipe_id: int = Path(None)):
    item = []
    if not item:
        raise HTTPException(status_code=404, detail=exceptions.ITEM_NOT_FOUND)
    return item


@router.get(RECIPES)
def get_all_recipes(ingredient: str = None, random: bool = False):
    # if not random then use page and offset
    return []