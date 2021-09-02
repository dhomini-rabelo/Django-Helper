def validate_unique(Model, field):
    # change field parameter e function name
    fields = list(Model.objects.filter(field=field))
    if len(fields) == 0:
        return True
    return False