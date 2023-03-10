from fastapi import APIRouter, Depends, HTTPException
from starlette import status

from api.endpoints import INGREDIENTS, INGREDIENT_BY_ID
from api.schemas import Ingredient
from services.ingredients_service import IngredientsService
from utils import validations, exceptions

router = APIRouter(tags=['Ingredients'])


@router.post(INGREDIENTS, status_code=status.HTTP_201_CREATED, response_model=None)
def create_ingredient(ingredient: Ingredient, service: IngredientsService = Depends(IngredientsService)):
    if validations.is_empty_name(ingredient.name):
        raise HTTPException(status_code=400, detail=exceptions.NAME_IS_REQUIRED)
    if not validations.is_valid_name(ingredient.name):
        raise HTTPException(status_code=400, detail=exceptions.INVALID_NAME)

    _, err = service.create_ingredient(ingredient.name)
    if err:
        raise HTTPException(status_code=err.status_code, detail=err.msg)


@router.put(INGREDIENT_BY_ID, status_code=status.HTTP_200_OK, response_model=None)
def update_ingredient(ingredient_id: int, ingredient: Ingredient, service: IngredientsService = Depends(IngredientsService)):
    if validations.is_empty_name(ingredient.name):
        raise HTTPException(status_code=400, detail=exceptions.NAME_IS_REQUIRED)
    if not validations.is_valid_name(ingredient.name):
        raise HTTPException(status_code=400, detail=exceptions.INVALID_NAME)

    _, err = service.update_ingredient(ingredient_id, ingredient.name)
    if err:
        raise HTTPException(status_code=err.status_code, detail=err.msg)


@router.get(INGREDIENTS, status_code=status.HTTP_200_OK, response_model=list)
def get_ingredients(limit: int = 10, offset: int = 0, service: IngredientsService = Depends(IngredientsService)):
    max_limit = 20
    if limit > max_limit:
        limit = max_limit
    if limit < 0:
        raise HTTPException(status_code=400, detail=exceptions.NUM_VALUE_MUST_NOT_BE_NEGATIVE.format(value='limit'))
    if offset < 0:
        raise HTTPException(status_code=400, detail=exceptions.NUM_VALUE_MUST_NOT_BE_NEGATIVE.format(value='offset'))
    result, err = service.get_ingredients(limit, offset)
    if err:
        raise HTTPException(status_code=err.status_code, detail=err.msg)
    return result
