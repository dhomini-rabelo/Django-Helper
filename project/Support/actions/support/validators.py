# django
from django.core.validators import validate_email
from django.core.validators import validate_slug, validate_unicode_slug 
from django.core.exceptions import ValidationError
# others
from string import ascii_letters, digits, punctuation




def validate_caracters(text: str, with_accents=True, spaces=True, use_symbols=True, use_numbers=True, use_underline=True):
    accents = 'áàéèíìóòúùâêîôûãõ' if with_accents else ''
    space = ' ' if spaces else ''
    symbols = punctuation if use_symbols else ''
    underline = "_" if use_underline else ''
    numbers = digits if use_numbers else ''
    alloweds = symbols + numbers + ascii_letters + accents + space + underline 
    for letter in text.lower():
       if letter not in alloweds:
           return False
    return True


def validate_for_email(email: str):
    try:
        validate_email(email)
        return True
    except ValidationError:
        return False
    
    
def validate_unique(Model, field_name: str, field):
    current_fields = Model.objects.values_list(field_name, flat=True)
    
    if field in current_fields:
        return False
    return True



def validate_for_slug(slug:str):
    if '/' in slug:
        return False
    try:
        validate_slug(slug)
        validate_unicode_slug(slug)
        return True
    except ValidationError:
        return False  
    


def validate_only_numeric(text):
    for letter in str(text):
        if letter not in list('123456789'):
            return False
    return True

    