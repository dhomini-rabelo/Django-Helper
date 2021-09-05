from exceptions import TypeNotFoundError, EqualTypeError

def convert_validation(initial_type:str, new_type:str):
    possible_types = ['str', 'int', 'decimal']
    if initial_type not in possible_types:
        raise TypeNotFoundError(f'{initial_type} type not identified')
    elif new_type not in possible_types:
        raise TypeNotFoundError(f'{new_type} type not identified')
