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


class UserCompareInput(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)

    top_choices = [
        ('big', '크다'),
        ('soso', '보통'),
        ('small', '작다'),
    ]

    bottom_choices = [
        ('big', '크다'),
        ('soso', '보통'),
        ('small', '작다'),
    ]
    
    chest_choices = [
        ('big', '크다'),
        ('soso', '보통'),
        ('small', '작다'),
    ]

    shoulder_choices = [
        ('big', '크다'),
        ('soso', '보통'),
        ('small', '작다'),
    ]

    arm_choices = [
        ('big', '크다'),
        ('soso', '보통'),
        ('small', '작다'),
    ]

    neck_choices = [
        ('big', '크다'),
        ('soso', '보통'),
        ('small', '작다'),
    ]

    waist_choices = [
        ('big', '크다'),
        ('soso', '보통'),
        ('small', '작다'),
    ]

    ass_choices = [
        ('big', '크다'),
        ('soso', '보통'),
        ('small', '작다'),
    ]

    thighs_choices = [
        ('big', '크다'),
        ('soso', '보통'),
        ('small', '작다'),
    ]
    
    top = models.CharField(max_length=6, choices=top_choices)
    bottom = models.CharField(max_length=6, choices=bottom_choices)
    chest = models.CharField(max_length=6, choices=chest_choices)
    shoulder = models.CharField(max_length=6, choices=shoulder_choices)
    arm = models.CharField(max_length=6, choices=arm_choices)
    neck = models.CharField(max_length=6, choices=neck_choices)
    waist = models.CharField(max_length=6, choices=waist_choices)
    ass = models.CharField(max_length=6, choices=ass_choices)
    thighs = models.CharField(max_length=6, choices=thighs_choices)

    def __str__(self):
        return f"top: {self.top}, bottom: {self.bottom}, chest: {self.chest}, shoulder: {self.shoulder}, arm: {self.arm}, neck: {self.neck}, waist: {self.waist}, ass: {self.ass}, thighs: {self.thighs}"