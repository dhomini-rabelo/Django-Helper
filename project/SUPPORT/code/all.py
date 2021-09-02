from .exceptions import TypeNotFound

def convert(obj, initial_type: str, new_type: str):
    possible_types = ['str', 'int', 'decimal']
    if initial_type not in possible_types:
        raise TypeNotFound(f'{initial_type} type not identified')
    elif new_type not in possible_types:
        raise TypeNotFound(f'{new_type} type not identified')
    elif initial_type == new_type:
        return obj
