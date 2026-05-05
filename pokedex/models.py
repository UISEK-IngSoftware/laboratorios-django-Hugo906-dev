from django.db import models

# Create your models here.

class Pokemon(models.Model):
    name = models.CharField(max_length=100, null=False)
    type = models.CharField(max_length=50, null=False)
    wight = models.FloatField()
    height = models.FloatField()
    
    def __str__(self):
        return self.name