from django import template


register = template.Library()


@register.filter(name='enumerate')
def _enumerate(iterable):
    return enumerate(iterable)


@register.filter(name='next')
def _next(obj):
    return next(obj)


@register.filter(name='get_item')
def _get_item(obj, index_):
    return obj[index_]


@register.filter(name='str')
def _str(obj):
    return str(obj)


@register.filter(name='br_money')
def _br_money(value):
    integer_value = str(value)[:-3]
    size = len(integer_value)
    representation = []
    count = 0
    for c in range(size-1, -1, -1):
        count += 1
        if count % 3 == 0 and count != size:
            representation.append(integer_value[c])
            representation.append('.')
        else:
            representation.append(integer_value[c])
    return ''.join(representation)[::-1] + f',{str(value)[-2:]}'