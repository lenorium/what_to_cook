from fastapi import Depends

from db.repositories.measures_repository import MeasuresRepository
from utils import exceptions


class MeasureService:
    def __init__(self, repository=Depends(MeasuresRepository)):
        self.repository = repository

    def create_measure(self, measure_name: str):
        res, err = self.repository.create_measure(measure_name)
        err = exceptions.map_exception(err)
        return res, err

    def update_measure(self, measure_id: int, new_name: str):
        res, err = self.repository.update_measure(measure_id, new_name)
        err = exceptions.map_exception(err)

        if not err and not res:
            err = exceptions.details(status_code=422, msg=exceptions.COULD_NOT_UPDATE)
        return res, err

    def get_measures(self, limit: int, offset: int):
        return self.repository.get_measures(limit, offset)
