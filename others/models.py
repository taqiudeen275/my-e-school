from django.db import models
from froala_editor.fields import FroalaField
from academics.models import Staff


class StaffPosition(models.Model):
    name = models.CharField(max_length=500)
    date_created = models.DateTimeField(auto_now_add=True)

    def  __str__(self):
        return self.name

class AboutStaff(models.Model):
    staff = models.ForeignKey(Staff, on_delete=models.CASCADE)
    year_employed = models.DateField(null=True,blank=True)
    position = models.ForeignKey(StaffPosition, on_delete=models.CASCADE, null=True, blank=True)
    discription = FroalaField(null=True, blank=True)
    date_added = models.DateTimeField(auto_now_add=True)

    class Meta:
        ordering = ['-date_added']

    def __str__(self):
        return f'About {self.staff}'

class NoticeBoard(models.Model):
    title = models.CharField(max_length= 500, null=True, blank=True)
    body = FroalaField()
    date_added = models.DateTimeField(auto_now_add=True)

    class Meta:
        ordering = ['-date_added']

    def __str__(self):
        return self.title

class SchoolHistory(models.Model):
    title = models.CharField(max_length= 500, null=True, blank=True)
    body = FroalaField()
    date_added = models.DateTimeField(auto_now_add=True)

    class Meta:
        ordering = ['-date_added']
    
    def __str__(self):
        return self.title

