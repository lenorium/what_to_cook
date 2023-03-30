from fastapi import Depends

from api import schemas
from api.schemas import Recipe
from db import models
from db.repositories.recipes_repository import RecipesRepository
from utils import exceptions


class RecipesService:
    def __init__(self, repository=Depends(RecipesRepository)):
        self.repository = repository

    def create_recipe(self, recipe: schemas.Recipe):
        db_quantities = [models.Quantity(q.quantity, q.measure_id, q.ingredient_id) for q in recipe.quantities]
        db_model = models.Recipe(recipe.name, recipe.description, db_quantities)
        res, err = self.repository.create_recipe(db_model)
        err = exceptions.map_exception(err)
        return res, err

    def update_recipe(self, recipe_id, recipe):
        res, err = self.repository.update_recipe(recipe_id, recipe)
        err = exceptions.map_exception(err)

        if not err and not res:
            err = exceptions.details(status_code=422, msg=exceptions.COULD_NOT_UPDATE)
        return res, err

