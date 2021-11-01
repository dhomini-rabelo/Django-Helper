# django
from django.contrib import auth


    
    
    
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
        return check_null(item)



def check_is_logged(request):
    user = auth.get_user(request)
    if user.is_authenticated():
        return True
    return False
