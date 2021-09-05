from utils import get_class
from support import convert_validation
from decimal import Decimal

def convert(obj, new_type: str):
    if new_type == 'pass': return 
    initial_type = get_class(obj)
    convert_validation(initial_type, new_type)
    if initial_type == 'str':
        if new_type == 'int':
            try: 
                return int(obj)
            except:
                return 'error'
        if new_type == 'decimal':
            try: 
                return Decimal(obj)
            except:
                return 'error'
            

obj = convert('1000.50', 'str')
print(obj, type(obj))


