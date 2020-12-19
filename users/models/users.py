"""User model."""

# Django
from django.db import models
from django.db.models.signals import post_save
from django.dispatch import receiver
from django.contrib.auth.models import AbstractUser
from django.core.validators import RegexValidator


# LearningPathAPI
#from learningPathAPI.models import LearningPath

# Utilities
from utils.models import LearningPathBackendModel


class User(LearningPathBackendModel, AbstractUser):
    """User model.

    Extend from Django's Abstract User, change the username field
    to email and add some extra fields.
    """

    email = models.EmailField(
        'email address',
        unique=True,
        error_messages={
            'unique': 'A user with that email already exists.'
        }
    )
    
    USERNAME_FIELD = 'email'
    REQUIRED_FIELDS = ['username', 'first_name', 'last_name']

    is_client = models.BooleanField(
        'client',
        default=True,
        help_text=(
            'Help easily distinguish users and perform queries. '
            'Clients are the main type of user.'
        )
    )

    is_verified = models.BooleanField(
        'verified',
        default=True,
        help_text='Set to true when the user have verified its email address.'
    )

    is_coach = models.BooleanField(
        'coach',
        default=False,
        help_text='Set to true when the user is a coach.'
    )

    """learningPath = models.OneToOneField(
        'LearningPath',
        on_delete=models.CASCADE,
        primary_key=True,
    )"""

    def __str__(self):
        """Return username."""
        return self.username

    def get_short_name(self):
        """Return username."""
        return self.username

