from django.core.exceptions import ValidationError
from django.utils.translation import gettext as _


def custom_password_validator(password):
    if len(password) < 8:
        raise ValidationError(_("Your password must be at least 8 characters long."))
    if password.isnumeric():
        raise ValidationError(_("Your password can't be entirely numeric."))
    if not any(char.isdigit() for char in password):
        raise ValidationError(_("Your password must contain at least one number."))
    if not any(char.isalnum() for char in password):
        raise ValidationError(_("Your password must contain at least one special character."))
