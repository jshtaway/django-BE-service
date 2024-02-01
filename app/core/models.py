"""
Database models.
"""
from django.db import models
from django.contrib.auth.models import (
    AbstractBaseUser,
    BaseUserManager,
    PermissionsMixin
)


# overriding BaseUserManager create_user method to remove username requirement
class UserManager(BaseUserManager):
    """Manager for users"""

    # overrides built in create_user function
    # now this function instead of built in function is called
    def create_user(self, email, password=None, **extra_fileds):
        """Create, save and return a new user."""
        user = self.model(email=email, **extra_fileds)
        user.set_password(password)
        user.save(using=self._db)
        return user


class User(AbstractBaseUser, PermissionsMixin):
    """User in the system."""
    email = models.EmailField(max_length=255, unique=True)
    name = models.CharField(max_length=255)
    is_active = models.BooleanField(default=True)
    is_staff = models.BooleanField(default=False)
    # replace username default field with the email custom field
    USERNAME_FIELD = 'email'