from django.db.models.signals import post_save,pre_save
from django.shortcuts import redirect
from django.dispatch import receiver
from account.models import User
from academics.models import Staff
from .models import StaffIDCode


@receiver(post_save, sender=User)
def staffUserConnector_handler(sender,created, instance, *args, **kwargs):
    if created or instance :
        if instance.user_type == "staff":
            q = Staff.objects.filter(user=instance)
            if not q.exists():
                Staff.objects.create(
                    user=instance,
                    first_name=instance.first_name,
                    last_name=instance.last_name,
                    )
        else:
            q = Staff.objects.filter(user=instance)
            if q.exists():
                q.delete()
    
@receiver(pre_save, sender=StaffIDCode)
def verificationID_handler(sender, instance,  *args, **kwargs):
    if instance :
        q = StaffIDCode.objects.filter(current=True)
        if q.exists():
            q.update(current=False)
            instance.current = True
        else:
            instance.current = True

@receiver(post_save, sender=Staff)
def isStaff_handler(sender, instance, *args, **kwargs):
    if instance:
        if instance.verified:
            user = User.objects.filter(id=instance.user.id)
            user.update(is_staff=True)