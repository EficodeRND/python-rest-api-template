import os
from functools import wraps


def check_api_key(**kwargs):
    api_key = os.environ.get('API_KEY', None)
    if api_key is None or ('api_key' in kwargs and kwargs['api_key'] == api_key):
        return True
    return False


def require_auth():
    def decorator(fn):
        @wraps(fn)
        def wrapper(*args, **kwargs):
            if not check_api_key(**kwargs):
                return 'Forbidden', 403
            return fn(*args, **kwargs)
        return wrapper
    return decorator
