from config.settings import get_settings

settings = get_settings()


class Notify:
    @staticmethod
    def send_confirmation_message(token: str):

        confirmation_url = f'{settings.HOST}:{settings.PORT}/auth/verify/{token}'
        message = f'''Hi!
Please confirm your registration: 

{confirmation_url}'''

        with open("hello.txt", "w", encoding="UTF-8") as f:
            f.write(message)
