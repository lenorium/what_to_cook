from fastapi import Depends

from db import database


class BaseRepository:
    def __init__(self, session=Depends(database.get_db)):
        self.session = session

    def add(self, entity):
        res, err = None, None
        try:
            self.session.add(entity)
            self.session.commit()
            self.session.refresh(entity)
            res = entity
        except Exception as e:
            err = e
        finally:
            return res, err

    def get_by_id(self, entity_type, entity_id):
        res, err = None, None
        try:
            res = self.session.get(entity_type, entity_id)
        except Exception as e:
            err = e
        finally:
            return res, err

    def get_all(self, entity_type, *filter, limit, offset=0):
        res, err = None, None
        try:
            res = self.session.query(entity_type)\
                .filter(*filter)\
                .limit(limit)\
                .offset(offset)\
                .all()
        except Exception as e:
            err = e
        finally:
            return res, err