from django.db import models
from django.contrib.auth.models import AbstractUser, Group, Permission

class User(AbstractUser):
    # Your other fields
    
    # Specify unique related_name arguments for the conflicting fields
    groups = models.ManyToManyField(Group, related_name='auth_user_groups')
    user_permissions = models.ManyToManyField(Permission, related_name='auth_user_permissions')


