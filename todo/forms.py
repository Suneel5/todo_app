from django import forms
from django.db.models.base import Model
# from .models import todo
class todoform(forms.Form):
    
    title=forms.CharField(max_length=50,label='todo')
    # class Meta:
    #     Model=todo
    #     fields='__all__'

