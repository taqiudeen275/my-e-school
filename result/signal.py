from django.db.models.signals import post_save,pre_save
from django.dispatch import receiver
from .models import SubjectResult,Result
from .views import get_position

# @receiver(post_save, sender=SubjectResult)
# def user_info_handler(sender,created,instance,*args, **kwargs):
#     if instance.completed:
#         position = get_position(instance.result_for, instance.clas_s, instance.student, instance.subject)
#         print(position)
        

        
      