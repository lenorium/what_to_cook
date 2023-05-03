from fastapi import APIRouter, HTTPException, Depends
from fastapi.params import Path
from starlette import status

from api.endpoints import RECIPE_BY_ID, RECIPES, RECIPE_RANDOM
from api.schemas import Recipe
from services.recipe_service import RecipesService
from utils import exceptions

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


@router.get(RECIPE_BY_ID, status_code=status.HTTP_200_OK, response_model=Recipe)
def get_recipe_by_id(recipe_id: int = Path(None), service: RecipesService = Depends(RecipesService)):
    res, err = service.get_recipe_by_id(recipe_id)
    if not res:
        raise HTTPException(status_code=404, detail=exceptions.ITEM_NOT_FOUND)
    if err:
        raise HTTPException(status_code=err.status_code, detail=err.msg)
    return res


@router.get(RECIPES, status_code=status.HTTP_200_OK, response_model=list[Recipe])
def get_all_recipes(limit: int = 10,
                    offset: int = 0,
                    service: RecipesService = Depends(RecipesService)):
    res, err = service.get_recipes(limit, offset)
    if err:
        raise HTTPException(status_code=err.status_code, detail=err.msg)
    return res


@router.get(RECIPE_RANDOM, status_code=status.HTTP_200_OK, response_model=list)
def get_random_recipe(service: RecipesService = Depends(RecipesService)):
    result, err = service.get_random_recipe()
    if err:
        raise HTTPException(status_code=err.status_code, detail=err.msg)
    return result
