# utils.py

from django.core.mail import send_mail
from django.conf import settings

def send_custom_email(subject, message, recipient_list):
    # The send_mail function sends the email
    send_mail(
        subject=subject,
        message=message,
        from_email=settings.EMAIL_HOST_USER,
        recipient_list=recipient_list,
        fail_silently=False,  # Set to True to suppress exceptions if the email fails to send
    )
