import pytest

from api.endpoints import MEASURES, MEASURE_BY_ID
from tests.fake_db import measure as fake_measure
from tests.base_test import client


@pytest.mark.parametrize('test_input', ['spn', 'big spn'])
def test_create_measure_positive(test_input):
    response = client.post(MEASURES, json={'name': test_input})
    assert response.status_code == 201


@pytest.mark.parametrize('test_input, expected', [('123', 'Name must contain only letters'),
                                                  ('', 'Name is required'),
                                                  (' ', 'Name is required')])
def test_create_measure_invalid_name(test_input, expected):
    response = client.post(MEASURES, json={'name': test_input})
    assert response.status_code == 400
    assert response.text == f'{{"detail":"{expected}"}}'


def test_put_measure_positive():
    response = client.put(MEASURE_BY_ID.format(
        measure_id=fake_measure.measure_id),
        json={'name': 'qwe'})
    assert response.status_code == 200


def test_put_measure_inexistent_id():
    response = client.put(MEASURE_BY_ID.format(
        measure_id=0),
        json={'name': 'qwe'})
    assert response.status_code == 422
    assert response.text == '{"detail":"Could not update"}'


def test_put_measure_non_unique_name():
    response = client.put(MEASURE_BY_ID.format(
        measure_id=fake_measure.measure_id),
        json={'name': fake_measure.name})
    assert response.status_code == 409


@pytest.mark.parametrize('test_input, expected', [('123', 'Name must contain only letters'),
                                                  ('', 'Name is required'),
                                                  (' ', 'Name is required')])
def test_put_measure_invalid_name(test_input, expected):
    response = client.put(MEASURE_BY_ID.format(
        measure_id=0),
        json={'name': test_input})
    assert response.status_code == 400
    assert response.text == f'{{"detail":"{expected}"}}'


@pytest.mark.parametrize('test_input', ['qwe', 1.1])
def test_put_measure_non_int_id(test_input):
    response = client.put(MEASURE_BY_ID.format(
        measure_id=test_input),
        json={'name': 'fake'})
    assert response.status_code == 422


def test_get_get_measures():
    response = client.get(MEASURES)
    assert response.status_code == 200


@pytest.mark.parametrize('test_input', ['qwe', 1.1])
def test_get_measures_non_int_limit(test_input):
    response = client.get(MEASURES, params={'limit': test_input})
    assert response.status_code == 422


def test_get_measures_negative_limit():
    response = client.get(MEASURES, params={'limit': -1})
    assert response.status_code == 400
    assert response.text == '{"detail":"limit must not be negative"}'


@pytest.mark.parametrize('test_input', ['qwe', 1.1])
def test_get_measures_non_int_offset(test_input):
    response = client.get(MEASURES, params={'offset': test_input})
    assert response.status_code == 422


def test_get_measures_negative_offset():
    response = client.get(MEASURES, params={'offset': -1})
    assert response.status_code == 400
    assert response.text == '{"detail":"offset must not be negative"}'
