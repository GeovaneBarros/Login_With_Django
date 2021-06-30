from django.db import models
from django.contrib.auth.models import User

class Cliente(models.Model):
    nome = models.CharField(max_length=32)
    sobrenome = models.CharField(max_length=32)
    user = models.OneToOneField(User, on_delete=models.CASCADE)
