from fastapi import Depends

import exceptions
from db import database


class BaseRepository:
    def __init__(self, session=Depends(database.get_db)):
        self.session = session

    def execute_sql_statement(self, sql_stmnt):
        res = None
        err = None
        try:
            res = self.session.execute(sql_stmnt)
        except Exception as e:
            err = exceptions.handle_exception(e)
        finally:
            return res, err
