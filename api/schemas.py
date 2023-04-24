from typing import Optional

from fastapi import HTTPException
from pydantic import BaseModel, validator, Field

from utils import exceptions


class ValidatedModel(BaseModel):
    @validator('name', check_fields=False)
    def transform(cls, value: str):
        if is_empty_name(value):
            raise HTTPException(status_code=400, detail=exceptions.NAME_IS_REQUIRED)
        if not is_valid_name(value):
            raise HTTPException(status_code=400, detail=exceptions.INVALID_NAME)
        return prepare_name(value)


class Measure(ValidatedModel):
    name: str

    class Config:
        orm_mode = True


class MeasureFull(Measure):
    measure_id: int


class Ingredient(ValidatedModel):
    name: str

    class Config:
        orm_mode = True


class IngredientFull(Ingredient):
    ingredient_id: int


class Quantity(BaseModel):
    ingredient_id: int
    quantity: int
    measure_id: int

    class Config:
        orm_mode = True


class Recipe(BaseModel):
    recipe_id = int
    name: str = Field(max_length=80)
    description: Optional[str]
    quantities: Optional[list[Quantity]] = []

    @validator('name')
    def check_name_not_empty(cls, value: str):
        if is_empty_name(value):
            raise HTTPException(status_code=400, detail=exceptions.NAME_IS_REQUIRED)
        return value

    class Config:
        orm_mode = True


def is_empty_name(value: str) -> bool:
    return value is None or value.strip() == ''


def is_valid_name(value: str) -> bool:
    # only space symbol and alpha letters are allowed
    return value.replace(' ', '').isalpha()


def prepare_name(value: str) -> str:
    return value.strip().lower()