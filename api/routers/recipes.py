from fastapi import APIRouter, HTTPException, Depends
from starlette import status

from api.endpoints import RECIPE_BY_ID, RECIPES
from api.schemas import Recipe
from services.recipe_service import RecipesService

router = APIRouter(tags=['Recipes'])


@router.post(RECIPES, status_code=status.HTTP_201_CREATED, response_model=Recipe)
def create_recipe(recipe: Recipe, service: RecipesService = Depends(RecipesService)):
    res, err = service.create_recipe(recipe)
    if err:
        raise HTTPException(status_code=err.status_code, detail=err.msg)
    return res


@router.put(RECIPE_BY_ID, status_code=status.HTTP_200_OK, response_model=Recipe)
def update_recipe(recipe_id: int, recipe: Recipe, service: RecipesService = Depends(RecipesService)):
    res, err = service.update_recipe(recipe_id, recipe)
    if err:
        raise HTTPException(status_code=err.status_code, detail=err.msg)
    return res


#
#
# @router.delete(RECIPE_BY_ID)
# def delete_recipe():
#     pass
#
#
# @router.get(RECIPE_BY_ID, status_code=status.HTTP_200_OK)
# def get_recipe_by_id(recipe_id: int = Path(None)):
#     item = []
#     if not item:
#         raise HTTPException(status_code=404, detail=exceptions.ITEM_NOT_FOUND)
#     return item
#
#
# @router.get(RECIPES)
# def get_all_recipes(ingredient: str = None, random: bool = False):
#     # if not random then use page and offset
#     return []
