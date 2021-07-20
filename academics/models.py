from django.db import models
from account.models import User

section_select = (
    ('A','A'),
    ('B','B'),
    ('C','C'),
    ('D','D'),
    ('E','E'),
    ('F','F'),
    ('G','G'),
    ('H','H'),
    ('I','I'),
    ('J','J'),
    ('K','K'),
    ('L','L'),
    ('M','M'),
    ('N','N'),
    ('O','O'),
    ('P','P'),
    ('Q','Q'),
    ('R','R'),
    ('S','S'),
    ('T','T'),
    ('U','U'),
    ('V','V'),
    ('W','W'),
    ('X','X'),
    ('Y','Y'),
    ('Z','Z')    
)
class Programme(models.Model):
    name = models.CharField(max_length=50)
    date = models.DateField(auto_now_add=True,null=True,blank=True)

    def __str__(self):
        return self.name

    class Meta:
        unique_together = ['name']
        verbose_name = "Program"
        verbose_name_plural = "Programs"
        ordering = ['-date']

track_select = (
    ('Track Gold', 'gold'),
    ('Track Green', 'green')
)

class Level(models.Model):
    name = models.IntegerField()

    def __str__(self):
        return self.name
    class Meta:
        unique_together = ['name']
        verbose_name = "Level"
        verbose_name_plural = "Levels"
        ordering = ['name']
        
         
class Class(models.Model):
    name = models.ForeignKey(Programme, on_delete=models.SET_NULL, null=True, blank=True)
    section = models.CharField(choices=section_select, max_length=1,null=True,blank=True)
    batch = models.ForeignKey('Batch', on_delete=models.SET_NULL, null=True,blank=True)
    track = models.CharField(choices=track_select, max_length=20,null=True,blank=True)
    date = models.DateField(auto_now_add=True)

    def __str__(self):
        return f'{self.name.name} {self.section} {self.batch} batch'

    class Meta:
        unique_together = ['name', 'batch', 'section', 'track']
        verbose_name = "Class"
        verbose_name_plural = "Classes"
        ordering = ['-date']

class Batch(models.Model):
    name = models.CharField(max_length=100)
    completed = models.BooleanField(default=False)
    date_added = models.DateTimeField(auto_now_add=True)
    def __str__(self):
        return self.name
    class Meta:
        unique_together = ['name']
        ordering = ['-date_added']


class Semester(models.Model):
    name = models.CharField(max_length=50)
    date_added = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.name
    class Meta:
        unique_together = ['name']
        ordering = ['-date_added']

class Academic_year(models.Model):
    name = models.CharField(max_length=50)
    date_added = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.name

    class Meta:
        unique_together = ['name']
        ordering = ['-date_added']

class Subject(models.Model):
  name = models.CharField(max_length=200, unique=True)

  class Meta:
    ordering = ['name']

  def __str__(self):
    return self.name



class Staff(models.Model):
    user = models.ForeignKey(User,related_name='staff', on_delete=models.SET_NULL, null=True,blank=True)
    first_name = models.CharField(max_length=45)
    last_name = models.CharField(max_length=45)
    staff_id = models.CharField(max_length=100, null=True, blank=True)
    photo = models.ImageField(blank=True,null=True)
    gender_choice = (
        ('male', 'Male'),
        ('female', 'Female'),
    )
    gender = models.CharField(choices=gender_choice, max_length=10)
    phone_number = models.CharField(max_length=11, unique=True,blank=True,null=True)
    email = models.CharField(max_length=255, unique=True,blank=True,null=True)
    date_joined = models.DateTimeField(null=True, blank=True)
    class_taught  = models.ManyToManyField(Class, blank = True)
    subject_taught = models.ForeignKey(Subject, on_delete=models.SET_NULL, null=True, blank = True)
    verified   = models.BooleanField(default=False)
    date = models.DateTimeField(auto_now_add=True)
    
    def __str__(self):
        return f'{self.first_name} {self.last_name}'

    class Meta:
        verbose_name = "Teacher"
        verbose_name_plural = "Teachers"
        ordering = ['-date']

class FormMaster(models.Model):
    staff = models.ForeignKey(Staff, on_delete=models.CASCADE, related_name='is_form_master')
    clas_s = models.ForeignKey(Class,on_delete=models.CASCADE)
    def __str__(self):
        return str(self.staff)
    class Meta:
        unique_together = ['staff']


