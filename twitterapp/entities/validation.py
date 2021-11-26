def validate(**kwargs):
    for k in kwargs.values():
        if k in "":
            return "Not Valid"
    return kwargs
