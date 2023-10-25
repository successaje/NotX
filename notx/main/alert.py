from django.db.models.signals import post_save
from django.dispatch import receiver
from datetime import date
from django.core.mail import send_mail

@receiver(post_save, sender=Alert)
def check_expiry_date(sender, instance, **kwargs):
    today = date.today()
    if instance.expiry_date <= today:
        user_email = instance.user.email  # Replace with how you associate users with products
        send_mail(
            'Product Expiry Alert',
            f'The product "{instance.name}" has reached its expiry date.',
            'from@example.com',
            [user_email],
            fail_silently=False,
        )