from django.db import models
from django import forms

# Create your models here.
class FormHistory(forms.Form):
    history = forms.CharField(label='history')