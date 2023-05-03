from enum import Enum


class Meal(Enum):
    BREAKFAST = 1
    BRUNCH = 2
    LUNCH = 4
    DINNER = 8
    SNACK = 16

    @classmethod
    def default(cls):
        return sum(map(lambda c: c.value, cls))
