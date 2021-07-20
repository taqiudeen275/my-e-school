from django.db.models.signals import post_save,pre_save
from django.shortcuts import redirect
from django.dispatch import receiver
from account.models import User
from academics.models import Staff
from .models import Student
import random
import string
from studentUser.models import StudentUser
from parent.models import Parent


@receiver(post_save, sender=Student)
def ID_handler(sender,created, instance, *args, **kwargs):
    if created or instance:
        if not instance.my_id :
            code = "".join(random.choice(string.ascii_uppercase + string.digits) for i in range(6))
            check = Student.objects.filter(my_id=code)
            if check.exists():
                code = "".join(random.choice(string.ascii_uppercase + string.digits) for i in range(7))
                instance.save()
                instance.my_id = code
            else:
                instance.my_id = code
                instance.save()

@receiver(post_save, sender=User)
def studentUserConnector_handler(sender,created, instance, *args, **kwargs):
    if created or instance :
        if instance.user_type == "student":
            q = StudentUser.objects.filter(user=instance)
            if not q.exists():
                StudentUser.objects.create(
                    user=instance,
                    )
        else:
            q = StudentUser.objects.filter(user=instance)
            if q.exists():
                student = Student.objects.filter(user=instance)
                student = student[0]
                student.user = None
                student.save()
                q.delete()

@receiver(post_save, sender=User)           
def parentUserConnector_handler(sender,created, instance, *args, **kwargs):
    if created or instance :
        if instance.user_type == "parent":
            q = Parent.objects.filter(user=instance)
            if not q.exists():
                Parent.objects.create(
                    user=instance,
                    )
        else:
            q = Parent.objects.filter(user=instance)
            if q.exists():
                q.delete()


