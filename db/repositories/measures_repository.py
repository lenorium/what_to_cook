from db.models import Measure
from db.repositories.base_repository import BaseRepository


class MeasuresRepository(BaseRepository):
    def create_measure(self, measure_name: str):
        return self.add(Measure(measure_name))

    def update_measure(self, measure_id: int, new_name: str):
        res, err = self.get_by_id(Measure, measure_id)
        if not res:
            return res, err

        res.name = new_name
        res, err = self.add(res)
        return res, err

    def get_measures(self, limit: int, offset: int):
        return self.get_all(Measure, limit=limit, offset=offset)
