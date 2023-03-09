from collections import namedtuple

from sqlalchemy.exc import IntegrityError

measures = namedtuple('measure', 'measure_id name')
measure = measures(measure_id=1, name='fake')


class FakeMeasureRepository:

    def create_measure(self, json):
        return None, None

    def update_measure(self, measure_id: int, json):
        if measure_id != measure.measure_id:
            return None, None
        if json == measure.name:
            fake_err = IntegrityError(None, orig=None, params=[])
            return None, fake_err
        else:
            return measure.measure_id, None

    def get_measures(self, limit, offset):
        return [], None
