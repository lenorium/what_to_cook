from db.models import Ingredient
from db.repositories.base_repository import BaseRepository


class IngredientsRepository(BaseRepository):
    def create_ingredient(self, name: str):
        return self.add(Ingredient(name))

    def update_ingredient(self, ingredient_id: int, new_name: str):
        res, err = self.get_by_id(Ingredient, ingredient_id)
        if not res:
            return res, err

        res.name = new_name
        res, err = self.add(res)
        return res, err

    def get_ingredients(self, limit: int, offset: int):
        return self.get_all(Ingredient, limit=limit, offset=offset)