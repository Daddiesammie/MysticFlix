# subscriber/utils.py
from django.core.mail import send_mail
from django.template.loader import render_to_string
from django.conf import settings

def send_new_video_email(subscriber_email, video_title):
    subject = 'New Video Uploaded'
    message = render_to_string('subscriber/new_video_email.html', {'video_title': video_title})
    
    send_mail(
        subject,
        '',
        settings.EMAIL_HOST_USER,
        [subscriber_email],
        html_message=message,
    )

