from django.db import models

class StaffIDCode(models.Model):
    name = models.CharField(max_length=10)
    current = models.BooleanField(default=False)
