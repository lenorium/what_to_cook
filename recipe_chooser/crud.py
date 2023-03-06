fake_db = {
    1: {'name': 'sandwich'},
    2: {'name': 'pancake'},
    3: {'name': 'scrambled egg'},
}


def get_recipe_by_id(recipe_id: int):
    return fake_db.get(recipe_id)


def get_recipes_by_filter():
    return []
