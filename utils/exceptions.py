from sqlalchemy.exc import IntegrityError, DataError
from collections import namedtuple

ITEM_NOT_FOUND = 'Item not found'
NAME_IS_REQUIRED = 'Name is required'
INVALID_NAME = 'Name must contain only letters'
COULD_NOT_UPDATE = 'Could not update'
NUM_VALUE_MUST_NOT_BE_NEGATIVE = '{value} must not be negative'

details = namedtuple('details', 'status_code msg')

exception_mapping = {
    IntegrityError: details(status_code=409, msg='Item already exists'),
    DataError: details(status_code=400, msg='Invalid entity')
}


def map_exception(e):
    if e:
        return exception_mapping\
            .get(type(e), details(500, 'Could not find exception type in mapping. See logs for details'))
