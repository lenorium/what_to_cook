from fastapi import Depends

from api import schemas
from db import models
from db.repositories.recipes_repository import RecipeRepository
from utils import exceptions


class RecipesService:
    def __init__(self, repository=Depends(RecipeRepository)):
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

    def get_recipes(self, limit: int, offset: int):
        return self.repository.get_recipes(limit, offset)

    def get_recipe_by_id(self, recipe_id):
        return self.repository.get_recipe_by_id(recipe_id)

    def get_random_recipe(self):
        return self.repository.get_random_recipe()
