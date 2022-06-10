from django.conf import settings
from django.core.mail import send_mail


def send_email(subject: str, text: str, email: str) -> None:
    try:
        send_mail(
            subject,
            text,
            settings.EMAIL_HOST_USER,
            [
                email
            ]
        )
    except Exception as exc:
        print(f'EMAIL_ERROR: {exc}')

