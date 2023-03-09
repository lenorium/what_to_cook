from pydantic import BaseModel


class Measure(BaseModel):
    name: str

    class Config:
        orm_mode: True


