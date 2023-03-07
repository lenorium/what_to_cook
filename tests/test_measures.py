from fastapi.testclient import TestClient

import exceptions
from api.endpoints import MEASURES
from app import app
from db.repositories.measures_repository import MeasuresRepository
from tests.fake_db import FakeMeasureRepository

app.dependency_overrides[MeasuresRepository] = FakeMeasureRepository


client = TestClient(app)


# def test_read_inexistent_recipe():
#     response = client.get(RECIPE_BY_ID.format(recipe_id=0))
#     assert response.status_code == 404
#     assert response.json() == {'detail': exceptions.ITEM_NOT_FOUND}
#
#
# def test_get_recipe():
#     response = client.get(RECIPE_BY_ID.format(recipe_id=1))
#     assert response.status_code == 200
    # assert response.json() == {'name': 'sandwich'}


# def test_get_recipes_by_ingredient():
#     response = client.get(RECIPES, params={'ingredient': ''})


def test_create_measure():
    json = {'name': 'spn'}
    response = client.post(MEASURES, json=json)
    assert response.status_code == 201


def test_create_multiple_words_measure():
    json = {'name': 'big spn'}
    response = client.post(MEASURES, json=json)
    assert response.status_code == 201


def test_create_empty_measure():
    json = {'name': ''}
    response = client.post(MEASURES, json=json)
    assert response.status_code == 400
    assert response.text == f'{{"detail":"{exceptions.NAME_IS_REQUIRED}"}}'


def test_create_space_measure():
    json = {'name': ' '}
    response = client.post(MEASURES, json=json)
    assert response.status_code == 400
    assert response.text == f'{{"detail":"{exceptions.NAME_IS_REQUIRED}"}}'


def test_create_numeric_measure():
    json = {'name': '123'}
    response = client.post(MEASURES, json=json)
    assert response.status_code == 400
    assert response.text == f'{{"detail":"{exceptions.INVALID_NAME}"}}'

