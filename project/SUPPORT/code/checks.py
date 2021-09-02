from decimal import Decimal
from detetime import datetime


def check_decimal(value):
    try:
        Decimal(1.00) + Decimal(value)
        return False
    except:
        return True
    

def check_date(date: str):
    try:
        date_check = str(datetime.strptime(date, '%Y-%m-%d').date())
        return date == date_check
    except:
        return False
    
    
def check_null(obj):
    try:
        if obj is None:
            return True
        elif isinstance(obj, str) and obj.strip() == '':
            return True
        elif len(obj) == 0:
            return True
    except TypeError:
        pass
    return False


def checks_null(input_list: list):
    for item in input_list:
        try:
            if item is None:
                return True
            elif isinstance(item, str) and item.strip() == '':
                return True
            elif len(item) == 0:
                return True
        except TypeError:
            pass
    return False
