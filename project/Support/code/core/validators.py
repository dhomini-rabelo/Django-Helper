from django.core.validators import validate_email, validate_integer
from string import ascii_letters, digits


def validate_caracteres_for_name(text: str, with_accents=True):
    accents = 'áàéèíìóòúùÀÁÈÉÌÍÒÓÙÚâêîôûÂÊÎÔÛãõÃÕ' if with_accents else ''
    symbols = "@.+-_"
    alloweds = symbols + digits + ascii_letters + accents
    print(alloweds)
    for letter in text:
       if letter not in alloweds:
           return False
    return True


def validate_for_email(email: str):
    try:
        validate_email(email)
        return True
    except:
        return False
    
    


    