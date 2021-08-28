from django.db import models
# from django.utils import timezone
from datetime import datetime
# Create your models here.

class task(models.Model):
    title=models.CharField(max_length=50)
    completed=models.BooleanField(default=False)
    date_created=models.DateTimeField(default=datetime.now().date())


    
    
