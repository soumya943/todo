from django.db import models

# Create your models here.
class Todo(models.Model):    
    name = models.CharField(max_length=30)
    notes = models.CharField(max_length=70)



































    

