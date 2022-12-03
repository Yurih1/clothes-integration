from pydantic import BaseModel


class UserData(BaseModel):
    """
    Parametros esperados para cadastrar novo usuário na base. (adicione conforme a necessidade)
    """
    username: str
    password: str
    
class FullDataUser(BaseModel):
    email: str
    full_name: str
    phone: str
    cpf: str
    rg: str       
    sexo: str
    logradouro: str
    number: str
    cep: str
    reference: str


class EmailUser(BaseModel):
    """
    Obtem o Email enviado no body.
    """
    email = str