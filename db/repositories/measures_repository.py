from db.models import Measure
from db.repositories.base_repository import BaseRepository


class MeasuresRepository(BaseRepository):
    def create_measure(self, measure_name: str):
        val = prepare_name(measure_name)

        sql_stmnt = f'''insert into {Measure.__tablename__} (name)
                        values ('{val}')'''

        _, err = self.execute_sql_statement(sql_stmnt)
        return err

    def update_measure(self, measure_id: int, new_name: str):
        val = prepare_name(new_name)

        sql_stmnt = f'''update {Measure.__tablename__}
                        set name = '{val}'
                        where measure_id = '{measure_id}'
                    '''
        _, err = self.execute_sql_statement(sql_stmnt)
        return err

    def get_measures(self, limit: int, offset: int):
        sql_stmnt = f'''select * 
                        from {Measure.__tablename__}
                        limit {limit} offset {offset}'''
        result, err = self.execute_sql_statement(sql_stmnt)
        return result.all(), err


def prepare_name(value: str):
    return value.strip().lower()
