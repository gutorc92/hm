from django.db import models
from django.utils.translation import ugettext as _

# Create your models here.
from django.contrib.auth.models import AbstractUser

class User(AbstractUser):

    email = models.EmailField(_('email address'), unique=True)

    USERNAME_FIELD = 'email'

    REQUIRED_FIELDS = ['first_name']
