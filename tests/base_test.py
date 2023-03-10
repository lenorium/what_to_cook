from starlette.testclient import TestClient

from app import app
from db.repositories.ingredients_repository import IngredientsRepository
from db.repositories.measures_repository import MeasuresRepository
from tests.fake_db import FakeMeasureRepository, FakeIngredientsRepository

app.dependency_overrides[MeasuresRepository] = FakeMeasureRepository
app.dependency_overrides[IngredientsRepository] = FakeIngredientsRepository


client = TestClient(app)
