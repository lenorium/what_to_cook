from fastapi.testclient import TestClient

import api
from api import app
import exception_msgs
from endpoints import RECIPES, RECIPE_BY_ID

client = TestClient(app)


def test_read_inexistent_recipe():
    response = client.get(RECIPE_BY_ID.format(recipe_id=0))
    assert response.status_code == 404
    assert response.json() == {'detail': exception_msgs.ITEM_NOT_FOUND}
    
    
def test_get_recipe():
    response = client.get(RECIPE_BY_ID.format(recipe_id=1))
    assert response.status_code == 200
    # assert response.json() == {'name': 'sandwich'}


# def test_get_recipes_by_ingredient():
#     response = client.get(RECIPES, params={'ingredient': ''})


