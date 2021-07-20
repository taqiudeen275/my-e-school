from django.db import models
from account.models import User
from student.models import Student


class StudentUser(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    student = models.ForeignKey(Student, on_delete=models.SET_NULL, blank=True, null=True)
    verified = models.BooleanField(default=False)

    def __str__(self):
        return str(self.user)