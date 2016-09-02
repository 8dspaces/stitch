from collections.abc import Mapping
from functools import wraps

def as_bool():
    def deco(func):
        @wraps(func)
        def wrapper(*args, **kwargs):
            self, value = args
            if isinstance(value, Mapping):
                assert value['t'] == 'MetaBool'
                value = value['c']
            result = func(self, value)
            return result
        return wrapper
    return deco


def as_choice(valid):
    def deco(func):
        @wraps(func)
        def wrapper(*args, **kwargs):
            self, value = args
            if isinstance(value, Mapping):
                value = ' '.join(x['c'] for x in value['c'])

            if value not in valid:
                msg = "`on_error` must be one of %s, got '%s' instead" % (
                    valid, value)
                raise TypeError(msg)

            result = func(self, value)
            return result
        return wrapper
    return deco


def as_string():
    def deco(func):
        @wraps(func)
        def wrapper(*args, **kwargs):
            self, value = args
            if isinstance(value, Mapping):
                value = ' '.join(x['c'] for x in value['c'] if x['c'])
            result = func(self, value)
            return result
        return wrapper
    return deco

