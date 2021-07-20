from django.db.models.signals import post_save,pre_save
from django.dispatch import receiver
from .models import Post


@receiver(pre_save, sender=Post)
def set_nxt_prev_post(sender,instance,*args, **kwargs):
    if instance:
        nextID = instance.id + 1
        prevID = instance.id
        if instance.id != 1:
            prevID = instance.id - 1
        prev_q = Post.objects.filter(id=prevID)
        if  prev_q.exists():
            instance.previous_post = prev_q[0] 

        next_q = Post.objects.filter(id=nextID)
        if  next_q.exists():
            instance.next_post = next_q[0]
            

   