from django.core.mail import send_mail


def send_activate_code(activate_code: str, email: str):
    title='Hello, this is activate link for your account on site Snakeshop'
    message=f'Please click link for activating account Http://127.0.0.1:8000/api/v1/account/activate/{activate_code}'
    from_email='SnakeShop@test.com'

    send_mail(title,message,from_email,[email], fail_silently=False,)