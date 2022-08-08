from django.contrib.auth.backends import ModelBackend
from ..apps.user.models import User


class EmailUsernameOrPhoneModelBackend(ModelBackend):

    """
    This is a Custom ModelBackend Authentication
    for either a phonenumber, username or an email address.
    """
    def authenticate(self, username=None, password=None):
        if '@' in username:
            kwargs = {'email': username}
        elif '+' in username:
            kwargs = {'phone': username}
        else:
            kwargs = {'username': username}
        try:
            user = User.objects.get(**kwargs)
            if user.check_password(password):
                return user
        except User.DoesNotExist:
            return None

    def get_user(self, username):
        try:
            return User.objects.get(pk=username)
        except User.DoesNotExist:
            return None

