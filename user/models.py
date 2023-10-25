from django.db import models

# Create your models here.

class UserBodyInput(models.Model):
    gender_choices = (
        ('male', '남성'),
        ('female', '여성'),
    )

    gender = models.CharField(max_length=6, choices=gender_choices)
    height = models.FloatField()
    weight = models.FloatField()


    def __str__(self):
        return f"({self.gender}), {self.height}cm, {self.weight}kg"