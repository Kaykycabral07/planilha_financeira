import re
import bcrypt
def verify_email(email: str) -> bool:
    """Verifica se o email está em um formato válido."""
    padrao = r'^[a-zA-Z0-9._%+-]+@[a-zA-Z0-9.-]+\.[a-zA-Z]{2,}$'
    return True if re.match(padrao, email) else False

def verify_password(password: str, confirm_password: str) -> bool:
    return True if password == confirm_password else False
    
def encrypt_password(password: str) -> bytes:
    return bcrypt.hashpw(password.encode("utf-8"), bcrypt.gensalt(12))

def check_password(stored_password: str, typed_password:str) -> bool:
    return bcrypt.checkpw(
        typed_password.encode("utf-8"),
        stored_password.encode("utf-8")
        )