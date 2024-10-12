import re

# Ввод email
email = input("Введите ваш email: ")

# Регулярное выражение для разбора email
pattern = r'(?P<username>[\w\.-]+)@(?P<domain>[\w\.-]+)'

match = re.match(pattern, email)

if match:
    username = match.group('username')
    domain = match.group('domain')
    print(f"username: {username}, domain: {domain}")
else:
    print("Некорректный email.")