from fastapi import Depends

from db.repositories.ingredients_repository import IngredientsRepository
from utils import exceptions


class IngredientsService:
    def __init__(self, repository=Depends(IngredientsRepository)):
        self.repository = repository

    def create_ingredient(self, ingredient_name: str):
        res, err = self.repository.create_ingredient(ingredient_name)
        err = exceptions.map_exception(err)
        return res, err

    def update_ingredient(self, ingredient_id: int, new_name: str):
        res, err = self.repository.update_ingredient(ingredient_id, new_name)
        err = exceptions.map_exception(err)

        if not err and not res:
            err = exceptions.details(status_code=422, msg=exceptions.COULD_NOT_UPDATE)
        return res, err

    def get_ingredients(self, limit: int, offset: int):
        return self.repository.get_ingredients(limit, offset)