from dataclasses import dataclass

from sqlalchemy.exc import IntegrityError


@dataclass
class Measure:
    measure_id: int
    name: str


@dataclass
class Ingredient:
    ingredient_id: int
    name: str


@dataclass
class Recipe:
    recipe_id: int
    name: str
    description: str
    quantities: list


recipe = Recipe(recipe_id=1, name='cake', description='delicious cake', quantities=[])
measure = Measure(measure_id=1, name='fake')
ingredient = Ingredient(ingredient_id=1, name='fake')


class FakeMeasureRepository:

    def create_measure(self, json):
        return measure, None

    def update_measure(self, measure_id: int, json):
        if measure_id != measure.measure_id:
            return None, None
        if json == measure.name:
            fake_err = IntegrityError(None, orig=None, params=[])
            return None, fake_err
        else:
            return measure, None

    def get_measures(self, limit, offset):
        return [], None


class FakeIngredientsRepository:

    def create_ingredient(self, json):
        return ingredient, None

    def update_ingredient(self, ingredient_id: int, json):
        if ingredient_id != ingredient.ingredient_id:
            return None, None
        if json == ingredient.name:
            fake_err = IntegrityError(None, orig=None, params=[])
            return None, fake_err
        else:
            return ingredient, None

    def get_ingredients(self, limit, offset):
        return [], None


class FakeRecipeRepository:
    def create_recipe(self, json):
        return recipe, None

    def update_recipe(self, recipe_id: int, json: str):
        if recipe_id != recipe.recipe_id:
            return None, None
        else:
            return recipe, None
