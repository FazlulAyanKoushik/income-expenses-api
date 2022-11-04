from django.db import models

from django.contrib.auth.models import (AbstractBaseUser, BaseUserManager, PermissionsMixin)
from django.db import models


'''
class UserManager(BaseUserManager):
    """
    Custom user model manager where email is the unique identifiers
    for authentication instead of usernames.
    """
    def create_user(self, email, password, **extra_fields):
        """
        Create and save a User with the given email and password.
        """
        if not email:
            raise ValueError(_('The Email must be set'))
        email = self.normalize_email(email)
        user = self.model(email=email, **extra_fields)
        user.set_password(password)
        user.save()
        return user
'''

class UserManager(BaseUserManager):
    def create_user(self, username, email, password=None):
        
        if username in None:
            raise ValueError('The username must be set')
        if email in None:
            raise ValueError('The email must be set')
        
        user = self.model(username=username, email=self.normalize_email(email))
        user.set_password(password)
        user.save()
        return user

    def create_superuser(self, username, email, password=None):
        if password is None:
            raise TypeError('Password should not be none')

        user = self.create_user(username, email, password)
        user.is_staff = True
        user.is_superuser = True
        if user.is_staff is not True:
            raise ValueError(_('Superuser must have is_staff=True.'))
        if user.is_superuser is not True:
            raise ValueError(_('Superuser must have is_superuser=True.'))
        user.save()
        return user
        
class User(AbstractBaseUser, PermissionsMixin):
    username = models.CharField(max_length=255, unique=True, db_index=True)
    email = models.EmailField(max_length=255, unique=True, db_index=True)
    is_verified = models.BooleanField(default=False)
    is_active = models.BooleanField(default=True)
    is_stuff = models.BooleanField(default=False)
    created_at = models.DateTimeField(auto_now_add=True)    # The auto_now_add will set the timezone.now() only when the instance is created.
    updated_at = models.DateTimeField(auto_now_add=True)    #On the other hand, the auto_now will update the field every time the save method is called.

    USERNAME_FIELD = 'email'
    REQUIRED_FIELDS = ['username']
        
    objects = UserManager()
        
    def __str__(self):
        return self.email
        
    def tokens(self):
        return ''