from sqlalchemy.exc import IntegrityError
from collections import namedtuple

ITEM_NOT_FOUND = 'Item not found'
NAME_IS_REQUIRED = 'Name is required'
INVALID_NAME = 'Name must contain only letters'

details = namedtuple('details', 'status_code msg')

exception_mapping = {
    IntegrityError: details(status_code=409, msg='Item already exists')
}


def handle_exception(e):
    return exception_mapping\
        .get(type(e), details(500, 'Could not find exception type in mapping. See logs for details'))
