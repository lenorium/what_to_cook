from fastapi import Depends

from utils import exceptions, validations
from db.repositories.measures_repository import MeasuresRepository


class MeasureService:
    def __init__(self, repository=Depends(MeasuresRepository)):
        self.repository = repository

    def create_measure(self, measure_name: str):
        val = validations.prepare_name(measure_name)
        _, err = self.repository.create_measure(val)
        err = exceptions.map_exception(err)
        return _, err

    def update_measure(self, measure_id: int, new_name: str):
        val = validations.prepare_name(new_name)
        res, err = self.repository.update_measure(measure_id, val)
        err = exceptions.map_exception(err)

        if not err and not res:
            err = exceptions.details(status_code=422, msg='Invalid measure_id')
        return res, err

    def get_measures(self, limit: int, offset: int):
        return self.repository.get_measures(limit, offset)
