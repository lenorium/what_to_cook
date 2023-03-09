from starlette.testclient import TestClient

from app import app
from db.repositories.measures_repository import MeasuresRepository
from tests.fake_db import FakeMeasureRepository

app.dependency_overrides[MeasuresRepository] = FakeMeasureRepository


client = TestClient(app)
