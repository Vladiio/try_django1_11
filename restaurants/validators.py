from django.core.exceptions import ValidationError


def validate_even(value):
    if value % 2 != 0:
        raise ValidationError(
            ('%(value)s is not an even number'),
            params={'value': value},
        )


CATEGORIES = ['Mexican', 'Asian', 'American', 'Whatever']

def validate_category(value):
    cat = value.capitalize()
    if not cat in CATEGORIES and not value in CATEGORIES:
        raise ValidationError(f"{value} is not a valid category")
    value = cat
