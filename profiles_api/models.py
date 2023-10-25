from django.db import models
from django.contrib.auth.models import AbstractBaseUser
from django.contrib.auth.models import PermissionsMixin
from django.contrib.auth.models import BaseUserManager

class UserProfileManager(BaseUserManager):
    """Manager for users profiles"""
    
    def create_user(self, email, name, password = None):
        """Create a new user profile"""
        if not email:
            raise ValueError('User must have an email address')
        
        email = self.normalize_email(email)
        user = self.model(email=email, name=name)
        
        user.set_password(password)
        user.save(using=self._db)
        
        return user
    
    def create_superuser(self, email, name, password):
        """Create and save a new superuser with given details"""
        user = self.create_user(email, name, password)
        
        user.is_superuser = True
        user.is_staff = True
        user.save(using=self._db)
        
        return user
        

# Create your models here.
class UserProfile(AbstractBaseUser, PermissionsMixin):
    """Database model for users in the system"""
    # Create a user manager class
    objects = UserProfileManager()

    # Create the fields for the user model
    email = models.EmailField(max_length=255, unique=True)
    name = models.CharField(max_length=255)
    # Create a field to determine if the user is active or not
    is_active = models.BooleanField(default=True)
    # Create a field to determine if the user is a staff member
    is_staff = models.BooleanField(default=False)

    # Set the username field to the email field
    USERNAME_FIELD = 'email'
    # Set the required fields
    REQUIRED_FIELDS = ['name']

    # Create a function to get the full name of the user
    def get_full_name(self):
        """Retrieve full name of user"""
        return self.name

    # Create a function to get the short name of the user
    def get_short_name(self):
        """Retrieve short name of user"""
        return self.name

    # Create a function to return the string representation of the user
    def __str__(self):
        """Return string representation of user"""
        return self.email