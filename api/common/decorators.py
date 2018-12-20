import traceback

from functools import wraps
from rest_framework.response import Response


def handle_exceptions(method):
    '''
    This decorator automatically handles api exceptions.
    '''
    @wraps(method)
    def wrapped(*args, **kwargs):
        try:
            resp = method(*args, **kwargs)
        except Exception:
            resp = Response({'status_code': 500,
                             'message': traceback.format_exc()})
        return resp
    return wrapped


# end of file
