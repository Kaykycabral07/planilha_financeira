import re

def verify_email(email: str) -> bool:
    """Verifica se o email está em um formato válido."""
    padrao = r'^[a-zA-Z0-9._%+-]+@[a-zA-Z0-9.-]+\.[a-zA-Z]{2,}$'
    return True if re.match(padrao, email) else False

def verify_password(password: str, confirm_password: str) -> bool:
    return True if password == confirm_password else False
    