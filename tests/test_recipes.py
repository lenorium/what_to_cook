import pytest

from api.endpoints import RECIPES, RECIPE_BY_ID
from tests.base_test import client
from tests.fake_db import recipe as fake_recipe


def test_create_recipe_positive_required_fields():
    response = client.post(RECIPES, json={'name': 'delicious cake'})
    assert response.status_code == 201


def test_create_recipe_positive_all_fields():
    response = client.post(RECIPES, json={'name': 'delicious cake',
                                          'description': 'alsjdhskajdh',
                                          'quantities': [{'ingredient_id': 1,
                                                          'quantity': 1,
                                                          'measure_id': 1}]})
    assert response.status_code == 201


def test_create_recipe_too_long_name():
    response = client.post(RECIPES, json={'name': 'q' * 81})
    assert response.status_code == 422


@pytest.mark.parametrize('test_input, expected', [('', 'Name is required'),
                                                  (' ', 'Name is required')])
def test_create_recipe_empty_name(test_input, expected):
    response = client.post(RECIPES, json={'name': test_input})
    assert response.status_code == 400
    assert response.text == f'{{"detail":"{expected}"}}'


def test_put_recipe_positive_required_fields():
    response = client.put(RECIPE_BY_ID.format(
        recipe_id=fake_recipe.recipe_id),
        json={'name': 'delicious cake'})
    assert response.status_code == 200


def test_put_recipe_positive_all_fields():
    response = client.put(RECIPE_BY_ID.format(
        recipe_id=fake_recipe.recipe_id),
        json={'name': 'delicious cake',
              'description': 'alsjdhskajdh',
              'quantities': [{'ingredient_id': 1,
                              'quantity': 1,
                              'measure_id': 1}]})
    assert response.status_code == 200
