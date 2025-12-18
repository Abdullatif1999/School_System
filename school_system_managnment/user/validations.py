from django.core.exceptions import ValidationError
from django.utils.translation import gettext_lazy as _
from django.core.validators import BaseValidator
from django.utils.deconstruct import deconstructible


@deconstructible
class PhoneValidations:

    def __call__(self , value):
        self.clean(value)
        
    def clean(self, value):
        if not value.startswith("+"):
            raise ValidationError(message="The phone number must start with + mark" , code="invalid" , params={"value": value})
        return value