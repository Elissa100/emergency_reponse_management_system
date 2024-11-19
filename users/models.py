from django.db import models
from django.contrib.auth.models import AbstractUser
from phonenumber_field.modelfields import PhoneNumberField

RWANDA_PROVINCES = [
    ('KIGALI', 'Kigali City'),
    ('NORTH', 'Northern Province'),
    ('SOUTH', 'Southern Province'),
    ('EAST', 'Eastern Province'),
    ('WEST', 'Western Province')
]

USER_TYPES = [
    ('ADMIN', 'Administrator'),
    ('RESPONDER', 'Emergency Responder'),
    ('REPORTER', 'Emergency Reporter'),
    ('COORDINATOR', 'Emergency Coordinator')
]

class CustomUser(AbstractUser):
    first_name = models.CharField(max_length=100)
    last_name = models.CharField(max_length=100)
    email = models.EmailField(unique=True)
    phone_number = PhoneNumberField(unique=True)
    user_type = models.CharField(max_length=20, choices=USER_TYPES)
    cell = models.CharField(max_length=100)
    district = models.CharField(max_length=100)
    province = models.CharField(max_length=20, choices=RWANDA_PROVINCES)
    
    def __str__(self):
        return f"{self.first_name} {self.last_name} - {self.user_type}"