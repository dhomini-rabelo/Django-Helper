from django.core.validators import validate_slug, validate_unicode_slug 
from validators import validate_for_email
from utils import get_type
from support import convert_validation
from decimal import Decimal
from datetime import datetime

def convert(obj, new_type: str):
    if new_type == 'pass': return 
    initial_type = get_type(obj)
    convert_validation(initial_type, new_type)
    if initial_type == 'str':
        if new_type == 'int':
            try: 
                return int(obj)
            except:
                return 'error'
        elif new_type == 'float':
            try: 
                return float(obj)
            except:
                return 'error'
        elif new_type == 'decimal':
            try: 
                return Decimal(obj)
            except:
                return 'error'
        elif new_type == 'bool':
            try:
                return bool(obj)
            except:
                return 'error'
        elif new_type == 'date':
            try:
                date_check = datetime.strptime(obj, '%Y-%m-%d').date()
                return obj
            except:
                return 'error'
        elif new_type == 'slug':
            try:
                validate_slug(obj)
                validate_unicode_slug(obj)
                return obj
            except:
                return 'error'        
        elif new_type == 'email':
            condition = validate_for_email(obj)
            return obj if condition else 'error'
    elif initial_type is None:
        return 'error'


