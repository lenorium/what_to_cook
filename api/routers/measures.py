from fastapi import APIRouter, Depends, HTTPException
from starlette import status

from api.endpoints import MEASURES, MEASURE_BY_ID
from api.schemas import Measure, MeasureFull
from services.measure_service import MeasureService
from utils import exceptions

router = APIRouter(tags=['Measures'])


@router.post(MEASURES, status_code=status.HTTP_201_CREATED, response_model=MeasureFull)
def create_measure(measure: Measure, service: MeasureService = Depends(MeasureService)):
    res, err = service.create_measure(measure.name)
    if err:
        raise HTTPException(status_code=err.status_code, detail=err.msg)
    return res


@router.put(MEASURE_BY_ID, status_code=status.HTTP_200_OK, response_model=MeasureFull)
def update_measure(measure_id: int, measure: Measure, service: MeasureService = Depends(MeasureService)):
    res, err = service.update_measure(measure_id, measure.name)
    if err:
        raise HTTPException(status_code=err.status_code, detail=err.msg)
    return res


@router.get(MEASURES, status_code=status.HTTP_200_OK, response_model=list[MeasureFull])
def get_measures(limit: int = 10, offset: int = 0, service: MeasureService = Depends(MeasureService)):
    max_limit = 50
    if limit > max_limit:
        limit = max_limit
    if limit < 0:
        raise HTTPException(status_code=400, detail=exceptions.NUM_VALUE_MUST_NOT_BE_NEGATIVE.format(value='limit'))
    if offset < 0:
        raise HTTPException(status_code=400, detail=exceptions.NUM_VALUE_MUST_NOT_BE_NEGATIVE.format(value='offset'))
    result, err = service.get_measures(limit, offset)
    if err:
        raise HTTPException(status_code=err.status_code, detail=err.msg)
    return result
