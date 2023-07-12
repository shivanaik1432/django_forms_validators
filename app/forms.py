from django import forms
from django.core import validators

class StudentForm(forms.Form):
    name=forms.CharField(max_length=100)
    age=forms.IntegerField()
    mail=forms.EmailField()
    remail=forms.EmailField()
    number=forms.CharField(max_length=10,min_length=10,validators=[validators.RegexValidator('[6-9]\d{9}')])