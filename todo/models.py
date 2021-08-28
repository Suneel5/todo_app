from django.db import models
from django.utils import timezone
# Create your models here.

class task(models.Model):
    title=models.CharField(max_length=50)
    completed=models.BooleanField(default=False)
    date_created=models.DateTimeField(default=timezone.now())


    
    
