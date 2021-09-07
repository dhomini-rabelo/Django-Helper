from .exceptions import TypeNotFoundError, EqualTypeError

def type_validation(initial_type:str, new_type:str):
    possible_types = ['str', 'int', 'decimal', 'bool', 'date', 'email',
                      'float', 'NoneType', 'slug']
    if initial_type not in possible_types:
        raise TypeNotFoundError(f'{initial_type} type not identified')
    elif new_type not in possible_types:
        raise TypeNotFoundError(f'{new_type} type not identified')


def adapt_form_errors(form_errors: dict):
    list_errors = []
    for name_for_error in form_errors['invalid_fields']:
        list_errors.append(f'O campo {name_for_error} é inválido')
    for name_for_error in form_errors['none_fields']:
        list_errors.append(f'O campo {name_for_error} não foi informado')
    for name_for_error in form_errors['repeated_fields']:
        list_errors.append(f'O campo {name_for_error} já está em uso')   
    for error in form_errors['other_errors']:
        list_errors.append(error)   
    return list_errors 
