

def simplification(obj_name: str):
    simplification = {'decimal.Decimal': 'decimal', 'datetime.date': 'date'}
    simplified_name = simplification.get(obj_name)
    if simplified_name is None:
        return obj_name
    else:
        return simplified_name


def get_type(obj):
    str_type = str(type(obj))
    initial_position = str_type.find("'")
    end_position = str_type[initial_position+1:].find("'") + len(str_type[: initial_position+1])
    class_name = str_type[initial_position+1:end_position]
    return simplification(class_name)

    
    


