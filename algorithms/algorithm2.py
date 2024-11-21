import re

def validate_email(email):
    """
    validates an email ID
    """
    email_regex = r'^[a-zA-Z0-9._%+-]+@[a-zA-Z0-9._]+\.[a-zA-Z]{2,}$'
    status = re.match(email_regex,email)
    return bool(status)