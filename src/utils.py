import re
def validar_id_usuario(id_usuario:str):
    """
    Valida que id_usuarios sea convertible a int
    Retorna True:False
    """
    # Completar
    return True

def validar_nombre(nombre:str):
    """
    Valida que nombre sea no nulo y que solo caracteres"""
    # Completar
    patron_nombre = r"[a-zA-Zéí ]*\d*"

    if re.fullmatch(patron_nombre, nombre) and len(nombre) > 0:
        return True
    return False

def validar_email(email:str):
    """
    Valida que email sea un correo válido"""
    # Completar
    patron_mail = r"[\w.+-]+@[\w-]+\.[a-zA-Z.]{2,}"
    return bool(re.fullmatch(patron_mail, email.strip()))
    