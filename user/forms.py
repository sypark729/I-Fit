# user_body_input_app/forms.py
from django import forms
from .models import UserBodyInput
    
class UserBodyInputForm(forms.ModelForm):
    class Meta:
        model = UserBodyInput
        fields = ['gender', 'height', 'weight']

    gender = forms.CharField()
    height = forms.FloatField(min_value=0)
    weight = forms.FloatField(min_value=0)