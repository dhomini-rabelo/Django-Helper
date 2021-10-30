# django
from django.core.exceptions import ValidationError
# this module
from exceptions import TypeNotFoundError
from validators import validate_unique, validate_for_email, validate_caracters, validate_for_slug, validate_only_numeric
# others
from datetime import datetime
from decimal import Decimal





def type_validation(initial_type:str, new_type:str):
    possible_types = ['str', 'int', 'decimal', 'bool', 'date',
                      'float', 'NoneType', 'slug']
    if initial_type not in possible_types:
        raise TypeNotFoundError(f'{initial_type} type not identified')
    elif new_type not in possible_types:
        raise TypeNotFoundError(f'{new_type} type not identified')




messages_form_errors = {
    'unique': 'Este campo já está em uso', 'exists': 'Este campo valor já foi cadastrado',
    'only_str': 'Este campo aceita apenas letras', 'only_numeric': 'Este campo aceita apenas números',
    'username': 'Este campo aceita apenas números, letras e underline',
    'min_length': lambda length: f'Este campo deve ter no mínimo {length} dígitos',
    'equal_length': lambda length: f'Este campo deve ter {length} dígitos',
    'max_length': lambda length: f'Este campo deve ter no máximo {length} dígitos',
    'slug': 'Este campo não pode ser representado por uma url, use apenas letras, hífen e underline',
    'email': 'Este email não está em um formato válido',
}




def adapt_form_errors(form_errors: dict):
    response = dict()
    for name in form_errors['invalid_fields']:
        response[name] = 'Este campo é inválido'
    for name in form_errors['none_fields']:
        response[name] = 'Este campo é obrigatório'
    for error, name, args in form_errors['other_errors']:
        if error in ['min_length', 'equal_length', 'max_length']:
            response[name] = messages_form_errors[error](args[1])
        else:
            response[name] = messages_form_errors[error]
    return response



def adapt_list_of_post_form(post_form_list: list):
    new_list = []
    for form_list in post_form_list:
        if len(form_list) == 3:
            model = form_list[:]
            model.append([])
            new_list.append(model)
        else:
            new_list.append(form_list)
    return new_list



convert_functions = {
    'str': lambda obj: str(obj), 'int': lambda obj: int(obj), 'float': lambda obj: float(obj),
    'decimal': lambda obj: Decimal(obj), 'date': lambda obj: datetime.strptime(obj, '%d/%m/%Y').date(),
}


other_errors_functions = {
    # model
    'unique': lambda Model, field_name, field: validate_unique(Model, field_name, field),
    'exists': lambda Model, field_name, field: not validate_unique(Model, field_name, field),
    # format
    'only_str': lambda field: validate_caracters(field, True, True, False, False),
    'username': lambda field: validate_caracters(field, False, False),
    'only_numeric': lambda field: validate_only_numeric(field), 
    'equal_length': lambda field, length: len(str(field)) == length,
    'min_length': lambda field, length: len(str(field)) >= length,
    'max_length': lambda field, length: len(str(field)) <= length,
    # value
    'email': lambda field: validate_for_email(field),
    'slug': lambda field: validate_for_slug(field),
}