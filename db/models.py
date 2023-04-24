from sqlalchemy import Column, Integer, String, ForeignKey, Table
from sqlalchemy.orm import declarative_base, relationship

from api.meals import Meal

Base = declarative_base()


class Ingredient(Base):
    __tablename__ = 'ingredients'

    ingredient_id = Column(Integer, primary_key=True, autoincrement=True)
    name = Column(String, unique=True, nullable=False)
    quantities = relationship('Quantity')

    def __init__(self, name):
        super().__init__()
        self.name = name


class Measure(Base):
    __tablename__ = 'measures'

    measure_id = Column(Integer, primary_key=True, autoincrement=True)
    name = Column(String, unique=True)
    quantities = relationship('Quantity')

    def __init__(self, name):
        super().__init__()
        self.name = name


class Recipe(Base):
    __tablename__ = 'recipes'

    recipe_id = Column(Integer, primary_key=True, autoincrement=True)
    name = Column(String(80), nullable=False)
    description = Column(String)
    meals = Column(Integer, default=Meal.default(), nullable=False)
    quantities = relationship('Quantity', cascade='all, delete-orphan')

    def __init__(self, name: str, description: str, meals: int, quantities: list):
        super().__init__()
        self.name = name
        self.description = description
        self.meals = meals
        self.quantities = quantities


class Quantity(Base):
    __tablename__ = 'quantities'

    # quantity_id = Column(Integer, primary_key=True, autoincrement=True, nullable=False)
    quantity = Column(Integer, nullable=False)
    recipe_id = Column(Integer, ForeignKey('recipes.recipe_id'), nullable=False, primary_key=True)
    measure_id = Column(Integer, ForeignKey('measures.measure_id'), nullable=False, primary_key=True)
    ingredient_id = Column(Integer, ForeignKey('ingredients.ingredient_id'), nullable=False, primary_key=True)

    def __init__(self, quantity, measure_id: int, ingredient_id: int):
        super().__init__()
        self.quantity = quantity
        self.measure_id = measure_id
        self.ingredient_id = ingredient_id