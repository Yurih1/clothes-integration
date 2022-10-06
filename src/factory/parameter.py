from pydantic import BaseModel
from typing import Union


class UserData(BaseModel):
    """
    Parametros esperados para cadastrar novo usuário na base. (adicione conforme a necessidade)
    """
    username: str
    password: str


class EmailUser(BaseModel):
    """
    Obtem o Email enviado no body.
    """
    mail = str