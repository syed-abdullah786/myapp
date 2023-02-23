from django.forms import ValidationError

def validate_file(value):
    value= str(value)
    if value.endswith(".pdf") != True:
        raise ValidationError("Only PDF can be uploaded")
    else:
        return value