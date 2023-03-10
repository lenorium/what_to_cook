import pytest

from api.endpoints import INGREDIENTS, INGREDIENT_BY_ID
from tests.base_test import client
from tests.fake_db import ingredient as fake_ingredient


@pytest.mark.parametrize('test_input', ['spn', 'big spn'])
def test_create_ingredient_positive(test_input):
    response = client.post(INGREDIENTS, json={'name': test_input})
    assert response.status_code == 201


@pytest.mark.parametrize('test_input, expected', [('123', 'Name must contain only letters'),
                                                  ('', 'Name is required'),
                                                  (' ', 'Name is required')])
def test_create_ingredient_invalid_name(test_input, expected):
    response = client.post(INGREDIENTS, json={'name': test_input})
    assert response.status_code == 400
    assert response.text == f'{{"detail":"{expected}"}}'


def test_put_ingredient_positive():
    response = client.put(INGREDIENT_BY_ID.format(
        ingredient_id=fake_ingredient.ingredient_id),
        json={'name': 'qwe'})
    assert response.status_code == 200


def test_put_ingredient_inexistent_id():
    response = client.put(INGREDIENT_BY_ID.format(
        ingredient_id=0),
        json={'name': 'qwe'})
    assert response.status_code == 422
    assert response.text == '{"detail":"Invalid id"}'


def test_put_ingredient_non_unique_name():
    response = client.put(INGREDIENT_BY_ID.format(
        ingredient_id=fake_ingredient.ingredient_id),
        json={'name': fake_ingredient.name})
    assert response.status_code == 409


@pytest.mark.parametrize('test_input, expected', [('123', 'Name must contain only letters'),
                                                  ('', 'Name is required'),
                                                  (' ', 'Name is required')])
def test_put_ingredient_invalid_name(test_input, expected):
    response = client.put(INGREDIENT_BY_ID.format(
        ingredient_id=0),
        json={'name': test_input})
    assert response.status_code == 400
    assert response.text == f'{{"detail":"{expected}"}}'


@pytest.mark.parametrize('test_input', ['qwe', 1.1])
def test_put_ingredient_non_int_id(test_input):
    response = client.put(INGREDIENT_BY_ID.format(
        ingredient_id=test_input),
        json={'name': 'fake'})
    assert response.status_code == 422


def test_get_get_ingredients():
    response = client.get(INGREDIENTS)
    assert response.status_code == 200


@pytest.mark.parametrize('test_input', ['qwe', 1.1])
def test_get_ingredients_non_int_limit(test_input):
    response = client.get(INGREDIENTS, params={'limit': test_input})
    assert response.status_code == 422


def test_get_ingredients_negative_limit():
    response = client.get(INGREDIENTS, params={'limit': -1})
    assert response.status_code == 400
    assert response.text == '{"detail":"limit must not be negative"}'


@pytest.mark.parametrize('test_input', ['qwe', 1.1])
def test_get_ingredients_non_int_offset(test_input):
    response = client.get(INGREDIENTS, params={'offset': test_input})
    assert response.status_code == 422


def test_get_ingredients_negative_offset():
    response = client.get(INGREDIENTS, params={'offset': -1})
    assert response.status_code == 400
    assert response.text == '{"detail":"offset must not be negative"}'
