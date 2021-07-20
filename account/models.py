from django.db import models
from django.contrib.auth.models import AbstractUser 


class User(AbstractUser):
    userType_select = (
        ('guest', 'Guest'),
        ('parent', 'Parent'),
        ('student', 'Student'),
        ('staff', 'Staff'),
    )
    photo = models.ImageField(upload_to='profile/', default='profile/default.png', blank=True,null=True)
    user_type = models.CharField(choices=userType_select, max_length=15)
    gender_select = (
        # ('----'),('----'),
        ('male', 'Male'),
        ('female', 'Female'),
    )
    gender = models.CharField(choices=gender_select, max_length=6, blank=True,null= True)

    def full_name(self):
        return f'{self.first_name} {self.last_name}'

# class Registration_no(models.Model):
#     user = models.OneToOneField(User, on_delete=models.CASCADE)
#     number = models.IntegerField(unique=True)