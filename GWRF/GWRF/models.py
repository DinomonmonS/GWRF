from django.db import models

class teacher(models.Model):
    name = models.CharField(max_length=25)
    Area = models.CharField(max_length=30)
