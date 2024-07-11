from django.db.models.signals import post_save
from django.dispatch import receiver
from .models import Series
from subscriber.models import Subscriber # type: ignore
from subscriber.utils import send_new_video_email # type: ignore

@receiver(post_save, sender=Series)
def notify_subscribers_on_new_movie(sender, instance, created, **kwargs):
    if created:
        subscribers = Subscriber.objects.all()
        for subscriber in subscribers:
            send_new_video_email(subscriber.email, instance.title)