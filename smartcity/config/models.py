from django.db import models

# Create your models here.

class Config(models.Model):
    name = models.CharField(max_length=100, unique=True, null=False)
    time = models.IntegerField(default=0, null=True, blank=True)

    def __str__(self):
        return self.name