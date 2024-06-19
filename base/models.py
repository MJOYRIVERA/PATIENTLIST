from django.db import models

# Create your models here.
class Patients(models.Model):
    
    name = models.CharField(max_length=100)
    illness = models.CharField(max_length=400)
    
    def __str__(self):
        return self.name