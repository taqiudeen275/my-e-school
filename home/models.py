from django.db import models
from django import forms
from froala_editor.fields import FroalaField

class Contact(models.Model):
    name = models.CharField(max_length=100)
    email = models.EmailField(max_length=254)
    message = models.TextField()
    
    def __str__(self):
        return self.email


class ProblemReport(models.Model):
    title = models.CharField(max_length=100, null=True, blank=True)
    body = FroalaField(null=True,blank=True)
    
    def __str__(self):
        return self.title
    