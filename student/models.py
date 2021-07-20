from django.db import models
from account.models import User
from academics.models import Batch,Class

class House(models.Model):
    name = models.CharField(max_length=300)
    date_added = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.name
accomodation_select = (
    ('DAY','Day'),
    ('BOARDING','Boarding'),
)


class Student(models.Model):
    user = models.ForeignKey(User,related_name='is_student', on_delete=models.SET_NULL, null=True,blank=True)
    first_name = models.CharField(max_length=200)
    last_name = models.CharField(max_length=200)
    middle_name = models.CharField(max_length=200, null=True, blank=True)
    photo = models.ImageField(upload_to='student-photos/', null=True, blank=True)
    date_of_birth = models.DateField()
    gender_choice = (
        ('male', 'Male'),
        ('female', 'Female'),
    )
    gender = models.CharField(choices=gender_choice, max_length=10)
    phone_number = models.CharField(max_length=11,null=True,blank=True)
    house = models.ForeignKey(House, null=True,blank=True, on_delete=models.SET_NULL)
    accomodation = models.CharField(choices=accomodation_select,max_length=50,null=True,blank=True )
    clas_s = models.ForeignKey(Class, on_delete=models.SET_NULL, null=True, blank=True, related_name='students')
    form = models.IntegerField(default=1)
    batch = models.ForeignKey(Batch,null=True, blank=True, on_delete=models.SET_NULL)
    completed = models.BooleanField(default=False)
    date_added = models.DateField(auto_now_add=True)
    my_id = models.CharField(max_length=6, null=True, blank=True)
    @property
    def full_name(self):
        return f'{self.first_name} {self.last_name}'
    

    def __str__(self):
        return f'{self.first_name} {self.last_name}'