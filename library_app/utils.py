import pyotp
from django.core.mail import send_mail
from django.contrib.auth.models import User

from library_app.models import OTP

def generate_otp(user_email):
    try:
        user = User.objects.get(email=user_email)
    except User.DoesNotExist:
        return None

    OTP.objects.filter(user=user, is_active=True).update(is_active=False)

    totp = pyotp.TOTP('hard-password')
    otp = totp.now()

    OTP.objects.create(user=user, otp_code=otp, is_active=True)

    send_mail(
        'Votre Code OTP',
        f'Voici votre code OTP: {otp}',
        'noreply@library.com',
        [user_email],
        fail_silently=False,
    )
    return otp

def validate_otp(user_email, otp_provided):
    from django.contrib.auth.models import User
    try:
        user = User.objects.get(email=user_email)
    except User.DoesNotExist:
        return False

    try:
        otp_record = OTP.objects.get(user=user, otp_code=otp_provided, is_active=True)
        otp_record.is_active = False
        otp_record.save()
        return True
    except OTP.DoesNotExist:
        return False