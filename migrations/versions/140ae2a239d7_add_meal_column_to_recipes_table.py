"""add meal column to recipes table

Revision ID: 140ae2a239d7
Revises: df39f3bd724c
Create Date: 2023-04-24 20:57:23.309886

"""
from alembic import op
import sqlalchemy as sa

from api.meals import Meal

# revision identifiers, used by Alembic.
revision = '140ae2a239d7'
down_revision = 'df39f3bd724c'
branch_labels = None
depends_on = None


def upgrade() -> None:
    # ### commands auto generated by Alembic - please adjust! ###
    op.add_column('recipes', sa.Column('meals', sa.Integer(), nullable=False, server_default=str(Meal.default())))
    # ### end Alembic commands ###


def downgrade() -> None:
    # ### commands auto generated by Alembic - please adjust! ###
    op.drop_column('recipes', 'meals')
    # ### end Alembic commands ###