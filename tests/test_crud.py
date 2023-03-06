import crud


def test_read_inexistent_recipe():
    assert crud.get_recipe_by_id(0) is None


def test_read_item():
    result = crud.get_recipe_by_id(1)
    assert result == {'name': 'sandwich'}

