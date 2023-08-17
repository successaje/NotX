from django.db import models
from django.contrib.auth.models import (AbstractBaseUser, BaseUserManager, PermissionsMixin)

from rest_framework_simplejwt.tokens import RefreshToken 

class UserManager(BaseUserManager):

    def create_user(self, username, first_name, last_name, store, email, password=None):

        if username is None:
            raise TypeError("Users should have a username")
        
        if first_name is None:
            raise TypeError('User should have a first name')

        if last_name is None:
            raise TypeError('User should have a last name')

        if store is None:
            raise TypeError("User should own a store")

        if email is None:
            raise TypeError("User should have an email")

        user = self.model(username=username,first_name=first_name, last_name = last_name, store = store, email=self.normalize_email(email))
        user.set_password(password)
        user.save()
        return user

    def create_superuser(self, username, first_name, last_name, email, store, password=None):

        if password is None:
            raise TypeError("Password shouldnt be none")

        user = self.create_user(username = username,first_name = first_name, last_name = last_name, email = self.normalize_email(email), password = password)
        user.is_superuser = True
        user.is_staff = True
        user.save()
        return user
    
class User(AbstractBaseUser, PermissionsMixin):
    username = models.CharField(max_length=255, unique=True, db_index = True)
    first_name = models.CharField(max_length = 255, default=True)
    last_name = models.CharField(max_length= 255, default = True)
    email = models.EmailField(max_length=255, unique=True, db_index=True)
    store = models.CharField(max_length=255, default=True)
    is_verified = models.BooleanField(default=False)
    is_staff = models.BooleanField(default = False)
    is_active = models.BooleanField(default=True)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    USERNAME_FIELD = 'email'
    REQUIRED_FIELDS = ['username', 'first_name', 'last_name', 'store']

    objects = UserManager()

    def __str__(self):
        return self.email
    
    