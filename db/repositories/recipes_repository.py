from db.models import Recipe
from db.repositories.base_repository import BaseRepository
import random


class RecipeRepository(BaseRepository):

    def create_recipe(self, recipe: Recipe):
        return self.add(recipe)

    def update_recipe(self, recipe_id, recipe: Recipe):
        res, err = self.get_by_id(Recipe, recipe_id)
        if not res:
            return res, err

        res.name = recipe.name
        res.description = recipe.description
        res.quantities = recipe.quantities
        res, err = self.add(res)
        return res, err

    def get_recipes(self, limit: int, offset: int):
        return self.get_all(Recipe, limit=limit, offset=offset)

    def get_recipe_by_id(self, recipe_id):
        return self.get_by_id(Recipe, recipe_id)

    def get_random_recipe(self):
        count = self.session.query(Recipe).count()

        offset = random.randint(0, count - 1)
        return self.get_all(Recipe, limit=1, offset=offset)
