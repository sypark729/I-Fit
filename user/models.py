from django.db import models
from django.contrib.auth.models import User

class UserBodyInput(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    gender_choices = [
        ('male', '남성'),
        ('female', '여성'),
    ]
    height = models.FloatField(default=0.0)
    weight = models.FloatField(default=0.0)
    gender = models.CharField(max_length=6, choices=gender_choices)

    def __str__(self):
        return f"{self.height}cm, {self.weight}kg, ({self.gender})"