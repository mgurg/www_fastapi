# from smtplib import SMTP
# from email.message import EmailMessage
import smtplib
from email.mime.text import MIMEText
from email.mime.multipart import MIMEMultipart
from email.mime.application import MIMEApplication
from ssl import create_default_context
from config.settings import get_settings

settings = get_settings()


class Mailer:
    def send_confirmation_message(token: str, mail_to: str):
        confirmation_url = f'{settings.HOST}:{settings.PORT}/auth/verify/{token}'
        message = f'''Hi!
Please confirm your registration: 

{confirmation_url}'''
        msg = MIMEMultipart()
        msg['From'] = 'info@tc.pl'
        msg['To'] = 'mgurgul@telecube.pl'
        msg['Subject'] ='Registration'

        msg_html = MIMEText(message, 'plain')
        msg.attach(msg_html)

        context = create_default_context()
        with smtplib.SMTP(settings.MAIL_HOST, settings.MAIL_PORT) as s:
            s.starttls(context=context)
            s.login(settings.MAIL_USERNAME, settings.MAIL_PASSWORD)
            s.sendmail('info@tc.pl', 'mgurgul@telecube.pl', msg.as_string())