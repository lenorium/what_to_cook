from db.models import Ingredient
from db.repositories.base_repository import BaseRepository


class IngredientsRepository(BaseRepository):
    def create_ingredient(self, ingredient_name: str):
        sql_stmnt = f'''insert into {Ingredient.__tablename__} (name)
                    values ('{ingredient_name}')
                    '''
        return self.execute_sql_statement(sql_stmnt)

    def update_ingredient(self, ingredient_id: int, new_name: str):
        sql_stmnt = f'''update {Ingredient.__tablename__}
                        set name = '{new_name}'
                        where ingredient_id = '{ingredient_id}'
                        returning ingredient_id
                    '''
        res, err = self.execute_sql_statement(sql_stmnt)

        if updated_row := res:
            updated_row = updated_row.first()

        return updated_row, err

    def get_ingredients(self, limit: int, offset: int):
        sql_stmnt = f'''select * 
                        from {Ingredient.__tablename__}
                        order by name
                        limit {limit} offset {offset}'''
        result, err = self.execute_sql_statement(sql_stmnt)
        return result.all(), err