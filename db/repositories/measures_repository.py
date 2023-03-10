from db.models import Measure
from db.repositories.base_repository import BaseRepository


class MeasuresRepository(BaseRepository):
    def create_measure(self, measure_name: str):
        sql_stmnt = f'''insert into {Measure.__tablename__} (name)
                        values ('{measure_name}')'''

        return self.execute_sql_statement(sql_stmnt)

    def update_measure(self, measure_id: int, new_name: str):
        sql_stmnt = f'''update {Measure.__tablename__}
                        set name = '{new_name}'
                        where measure_id = '{measure_id}'
                        returning measure_id
                    '''
        res, err = self.execute_sql_statement(sql_stmnt)

        if updated_row := res:
            updated_row = updated_row.first()

        return updated_row, err

    def get_measures(self, limit: int, offset: int):
        sql_stmnt = f'''select * 
                        from {Measure.__tablename__}
                        order by name
                        limit {limit} offset {offset}'''
        result, err = self.execute_sql_statement(sql_stmnt)
        return result.all(), err
