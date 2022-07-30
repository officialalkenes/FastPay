from django.db import models

from django.utils.translation import gettext_lazy as _

from django.contrib.auth.models import AbstractBaseUser, PermissionsMixin

from .managers import UserManager
from .validators import mobile_regex
# Create your models here.
class User(AbstractBaseUser, PermissionsMixin):
    """
        phonenumber field adopts regex phone number configuration since configuration is  based on local Banking system
    """

    email = models.EmailField(unique=True, verbose_name=_("Email Address"),
                              help_text=_("Provide a Valid Email Address")
                              )
    username = models.CharField(max_length=100, verbose_name=_("Username"),
                                unique=True)
    # phone_format = models.CharField(max_length=5, default='+234',
    #                                 help_text=_("format: required, Nigerian Only"))
    phone_number = models.CharField(max_length=10, validators=mobile_regex,
                                    help_text="format: required, regex-format: +234 (12345678)")
    fullname = models.CharField(max_length=100, verbose_name=_("Full Name"))
    is_staff = models.BooleanField(
        _('staff status'),
        default=False,
        help_text=_('Designates whether the user can log into this admin site.'),
    )
    is_active = models.BooleanField(
        _('active'),
        default=True,
        help_text=_(
            'Designates whether this user should be treated as active. '
            'Unselect this instead of deleting accounts.'
        ),
    )
    date_joined = models.DateTimeField(_('Date Joined'), auto_now_add=True)
    last_login = models.DateTimeField(_('Last Login Date'), auto_now=True)

    verified =models.BooleanField(verbose_name=_('Verify Email'),
        default=False,
        help_text=_(
                "Designates whether this user's email has been Verified. "
        ),
    )

    USERNAME_FIELD = 'email'
    REQUIRED_FIELDS = ('username', 'fullname')

    objects = UserManager()

    class Meta:
        verbose_name = 'User'
        verbose_name_plural = 'Users'

    @property
    def get_shortname(self):
        return f'{self.username}'

    def __str__(self) -> str:
        return f'{self.get_shortname}'

    # def get_absolute_url(self):
    #     return reverse("model_detail", kwargs={"pk": self.pk})
