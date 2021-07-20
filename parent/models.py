from django.db import models
from student.models import  Student
from account.models import User

class Parent(models.Model):
    user = models.ForeignKey(User, related_name = 'is_parent', on_delete=models.CASCADE)
    student = models.ManyToManyField(Student,related_name='parent')
    verified = models.BooleanField(default=False)

    def __str__(self): 
        return str(self.user)
    