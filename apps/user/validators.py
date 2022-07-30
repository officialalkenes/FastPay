from django.core.validators import RegexValidator

"""
    For Mobile Phone Verification => Min length 11, Max Length 15
"""
mobile_regex = RegexValidator(regex=r'^\+?1?\d{1,3}?\,?\s?\d{11,15}$', message="Phone number must not consist of space and requires country code. eg : +6591258565")
