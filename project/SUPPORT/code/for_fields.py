from django.core.validators import validate_slug, validate_unicode_slug 


def set_slug(slug: str):
    invalid_letters = list()
    slug = slug.replace('_',' ').replace('-',' ')
    slug_list = [letter for letter in slug]
    for letter in slug_list:
        try:
            validate_slug(letter)
            validate_unicode_slug(letter)
        except:
            invalid_letters.append(letter)
    for letter in invalid_letters:
        slug_list.remove(letter)
    return "".join(slug_list)



    
    
