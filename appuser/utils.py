from django.core.mail import send_mail
import pyotp


def generate_otp ():
    secret_key = pyotp.random_base32()
    totp = pyotp.TOTP(secret_key)
    otp = totp.now()
    return otp


def send_otp_email(email, otp):
     send_mail(
            "Password Reset Request: Verify Your Email",
            f'Here is your OTP: {otp}, go back to the site and input for verification',
            "VEEPAY <veepay.ng@gmail.com>",
            [email],
            fail_silently=False,
        )
