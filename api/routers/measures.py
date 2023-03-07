from fastapi import APIRouter, Depends, HTTPException
from starlette import status

import exceptions
from api.schemas import Measure
from db.repositories.measures_repository import MeasuresRepository
from api.endpoints import MEASURES, MEASURE_BY_ID

router = APIRouter(tags=['Measures'])


@router.post(MEASURES, status_code=status.HTTP_201_CREATED, response_model=None)
def create_measure(measure: Measure, db: MeasuresRepository = Depends(MeasuresRepository)):
    if is_empty_name(measure.name):
        raise HTTPException(status_code=400, detail=exceptions.NAME_IS_REQUIRED)
    if not is_valid_name(measure.name):
        raise HTTPException(status_code=400, detail=exceptions.INVALID_NAME)

    err = db.create_measure(measure.name)
    if err:
        raise HTTPException(status_code=err.status_code, detail=err.msg)


@router.put(MEASURE_BY_ID, status_code=status.HTTP_200_OK)
def update_measure(measure_id: int, measure: Measure, db: MeasuresRepository = Depends(MeasuresRepository)):
    if is_empty_name(measure.name):
        raise HTTPException(status_code=400, detail=exceptions.NAME_IS_REQUIRED)
    if not is_valid_name(measure.name):
        raise HTTPException(status_code=400, detail=exceptions.INVALID_NAME)

    err = db.update_measure(measure_id, measure.name)
    if err:
        raise HTTPException(status_code=err.status_code, detail=err.msg)


@router.get(MEASURES, status_code=status.HTTP_200_OK)
def get_measures(limit: int = 10, offset: int = 0, db: MeasuresRepository = Depends(MeasuresRepository)):
    #TODO проверка на максимальный limit
    result, err = db.get_measures(limit, offset)
    if err:
        raise HTTPException(status_code=err.status_code, detail=err.msg)
    return result


def is_empty_name(value: str) -> bool:
    return value is None or value.strip() == ''


def is_valid_name(value: str) -> bool:
    return value.isalpha()

