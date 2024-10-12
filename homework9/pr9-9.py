import re


email_pattern = r"^([a-zA-Z0-9_.+-]+)@([a-zA-Z0-9-]+\.[a-zA-Z0-9-.]+)$"


def parse_email(email):
    match = re.match(email_pattern, email)
    if match:
        username, domain = match.groups()
        return username, domain
    else:
        return None

