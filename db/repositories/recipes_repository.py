from db.models import Recipe
from db.repositories.base_repository import BaseRepository


class RecipesRepository(BaseRepository):

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


