from decimal import Decimal


def simplification(obj_name: str):
    simplification = {'decimal.Decimal': 'decimal'}
    simplified_name = simplification.get(obj_name)
    if simplified_name is None:
        return obj_name
    else:
        return simplified_name


def get_class(obj):
    str_class = str(type(obj))
    initial_position = str_class.find("'")
    end_position = str_class[initial_position+1:].find("'") + len(str_class[: initial_position+1])
    class_name = str_class[initial_position+1:end_position]
    return simplification(class_name)

    
    


