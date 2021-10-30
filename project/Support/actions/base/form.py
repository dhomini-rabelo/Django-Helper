# django
# this module
from validators import validate_for_email, validate_unique, validate_caracters
from utils import get_type
from support import type_validation, adapt_form_errors, adapt_list_of_post_form
from functions_dict import convert_functions, other_errors_functions
from checks import check_null
# others
from decimal import InvalidOperation
from datetime import datetime



def convert(obj, new_type: str):
    convert_process = convert_functions[new_type]
    
    if obj is not None:
        return convert_process(obj)
    else:
        return None



def convert_validation(field, new_type: str):
    if new_type == 'pass': return 'valid'
    try:
        validation = convert(field, new_type)
        return validation if validation is not None else 'convert_error'
    except (ValueError, InvalidOperation):
        return 'convert_error'
        
      
        
def get_post_form_errors(fields: list):
    """
    Form list fields
    [
    [value, type, field_name, [(other_validation, *args),]],
    ]
    """
    # errors
    invalid_fields, none_fields, other_errors = [], [], []
    types_for_others_validations = [
        'unique', 'exists', 'only_str', 'only_numeric', 'email', 'caracters', 'min-max-equal(length)',
        'username', 'slug',
    ]
    
    for field, convert_var, name, more_validations in adapt_list_of_post_form(fields):
        formated_field = convert_validation(field, convert_var)

        if check_null(field):
            none_fields.append(name)  
        elif str(formated_field) == 'convert_error':
            invalid_fields.append(name)
        else:
            for other_validation in more_validations:
                args = [*other_validation[1:]]
                args.insert(0, formated_field)
                validation = other_errors_functions[other_validation[0]]
                if not validation(*args):
                    other_errors.append([other_validation[0], name, args])
                
    form_errors = {'invalid_fields': invalid_fields, 'none_fields': none_fields,
                    'other_errors': other_errors}
    
    form_errors = adapt_form_errors(form_errors)
    return form_errors if form_errors != {} else None


    
def get_password_error(password: str, confirm_password: str):
    if not password == confirm_password:
        return (0, 'As senhas são diferentes')
    return None


def change_password(user, current_password: str, new_password: str, new_password_confirm: str):
    errors_list = list()
    if not user.check_password(current_password):
        errors_list.append('Senha incorreta')
    else:
        error_password = get_password_error(new_password, new_password_confirm)
        if error_password is None:
            user.set_password(new_password)
            user.save()
        errors_list.append(error_password[1])
    return errors_list if errors_list != [] else None
    
