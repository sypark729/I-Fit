from django.db import models

# Create your models here.

class UserBodyInput(models.Model):
    gender_choices = (
        ('male', '남성'),
        ('female', '여성'),
    )

    height = models.FloatField()
    weight = models.FloatField()
    gender = models.CharField(max_length=6, choices=gender_choices)

    def __str__(self):
        return f"{self.height}cm, {self.weight}kg, ({self.gender})"