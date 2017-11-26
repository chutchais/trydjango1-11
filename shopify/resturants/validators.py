from django.core.exceptions import ValidationError
# from django.utils.translation import ugettext_lazy as _

def validate_even(value):
    if value % 2 != 0:
        raise ValidationError(
            _('%(value)s is not an even number'),
            params={'value': value},
        )

def validate_email(value):
	email = value
	if ".edu" in email:
		raise ValidationError('We do not accept edu email')


CATEGORIES = ['Maxican','Asian','American']

def validate_category(value):
	if not value in CATEGORIES:
		raise ValidationError(f'{value} is not a valid category')