from django import forms
from django.db.models.base import Model
from .models import task
class todoform(forms.ModelForm):
    # title=forms.CharField(max_length=50,label='todo')
    class Meta:
        model=task
        fields=['title']

    