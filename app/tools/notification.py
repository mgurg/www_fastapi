

class Notify:
    @staticmethod
    def send_confirmation_message(token: str):

        confirmation_url = '{}{}/auth/verify/{}'.format("http://127.0.0.1", 'auth', token)
        message = '''Hi!
Please confirm your registration: {}.'''.format(confirmation_url)

        with open("hello.txt", "w", encoding="UTF-8") as f: 
            f.write(message) 