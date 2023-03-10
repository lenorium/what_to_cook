from fastapi import Depends

from db.repositories.ingredients_repository import IngredientsRepository
from utils import validations, exceptions


class IngredientsService:
    def __init__(self, repository=Depends(IngredientsRepository)):
        self.repository = repository

    def create_ingredient(self, ingredient_name: str):
        val = validations.prepare_name(ingredient_name)

        _, err = self.repository.create_ingredient(val)
        err = exceptions.map_exception(err)
        return _, err

    def update_ingredient(self, ingredient_id: int, new_name: str):
        val = validations.prepare_name(new_name)
        res, err = self.repository.update_ingredient(ingredient_id, val)
        err = exceptions.map_exception(err)

        if not err and not res:
            err = exceptions.details(status_code=422, msg=exceptions.INVALID_ID)
        return res, err

    def get_ingredients(self, limit: int, offset: int):
        return self.repository.get_ingredients(limit, offset)