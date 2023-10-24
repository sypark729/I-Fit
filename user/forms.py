# user_body_input_app/forms.py
from django import forms
from .models import UserBodyInput

class UserBodyInputForm(forms.ModelForm):
    class Meta:
        model = UserBodyInput
        fields = ['height', 'weight', 'gender']