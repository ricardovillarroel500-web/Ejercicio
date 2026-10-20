import re
def validar_id_usuario(id_usuario:str):
    """
    Valida que id_usuarios sea convertible a int
    Retorna True:False
    """
    patron_id = r"[1-9][0-9]*"
    return bool(re.fullmatch(patron_id, id_usuario))
    # Completar



def validar_nombre(nombre:str):
    """
    Valida que nombre sea no nulo y que solo caracteres"""
    patron_nombre = r"[a-zA-Zéí ]*\d*"

    if re.fullmatch(patron_nombre, nombre) and len(nombre) > 0:
        return True
    return False

def validar_email(email: str):
    patron_mail = r"[\w.+-]+@[\w-]+\.[a-zA-Z.]{2,}"
    return bool(re.fullmatch(patron_mail, email.strip()))
