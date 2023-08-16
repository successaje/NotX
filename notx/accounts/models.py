from django.db import models
from django.contrib.auth.models import (AbstractBaseUser, BaseUserManager, PermissionsMixin)

from rest_framework_simplejwt.tokens import RefreshToken 

class UserManager(BaseUserManager):

    def create_user(self, username, first_name, last_name, email, password=None):

        if username is None:
            raise TypeError("Users should have a username")
        
        if first_name is None:
            raise TypeError('User should have a first name')

        if last_name is None:
            raise TypeError('User should have a last name')


        if email is None:
            raise TypeError("User should have an email")

        user = self.model(username=username,first_name=first_name, last_name = last_name, email=self.normalize_email(email))
        user.set_password(password)
        user.save()
        return user

    def create_superuser(self, username, first_name, last_name, email, password=None):

        if password is None:
            raise TypeError("Password shouldnt be none")

        user = self.create_user(username = username,first_name = first_name, last_name = last_name, email = self.normalize_email(email), password = password)
        user.is_superuser = True
        user.is_staff = True
        user.save()
        return user