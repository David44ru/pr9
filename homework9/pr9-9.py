import re

# Регулярное выражение для разделения email на имя пользователя и домен
email_pattern = r"^([a-zA-Z0-9_.+-]+)@([a-zA-Z0-9-]+\.[a-zA-Z0-9-.]+)$"

# Функция для парсинга email
def parse_email(email):
    match = re.match(email_pattern, email)
    if match:
        username, domain = match.groups()
        return username, domain
    else:
        return None

# Цикл для повтора программы
while True:
    # Ввод email пользователя
    email = input("Введите ваш email: ")

    