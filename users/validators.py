from django.core.exceptions import ValidationError
from django.utils.translation import gettext as _

class DigitValidator:
    def validate(self, password, user=None):
        """
        Checks if the password contains a digit
        """
        contains_digit = False
        for digit in "0123456789":
            if digit in password:
                contains_digit = True
                break

        if not contains_digit:
            raise ValidationError(
                _("Password must contain at least 1 digit."),
                code="all_chars_password",
            )

class LowerCaseValidator:
    def validate(self, password, user=None):
        """
        Checks if  the password contains a lowercase char
        """
        contains_lower_char = False

        for char in "abcdefghijklmnopqrstuvwxyz":
            if char in password:
                contains_lower_char = True
                break

        if not contains_lower_char:
            raise ValidationError(
                _("Password must contain at least 1 lowercase character."),
                code="all_chars_uppercase",
            )

class UpperCaseValidator:
    def validate(self, password, user=None):
        """
        Checks if  the password contains a uppercase char
        """
        contains_upper_char = False

        for char in "ABCDEFGHIJKLMNOPQRSTUVWXYZ":
            if char in password:
                contains_upper_char = True
                break

        if not contains_upper_char:
            raise ValidationError(
                _("Password must contain at least 1 uppercase character."),
                code="all_chars_lowercase",
            )

class SymbolValidator:
    def validate(self, password, user=None):
        """
        Checks if  the password contains a symbol
        """
        contains_symbol = False

        for char in "!\"#$%&'()*+,-./:;<=>?@[\]^_`{|}~.":
            if char in password:
                contains_symbol = True
                break

        if not contains_symbol:
            raise ValidationError(
                _("Password must contain at least 1 symbol."),
                code="no_symbols",
            )