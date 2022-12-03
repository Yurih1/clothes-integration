from contact_handlers.repository import UserRepository
from utils.helpers import ContactHelpers


class User:
    """
    Classe resposável por modelas algumas informações do usuario.
    """
    def __init__(self, email: str) -> None:

        self.repository = UserRepository(email)
        self.email = email
        
    def post_new_contact(self, post_data: dict):
        self.repository.create_new_contact(post_data)
    
    def update_password(self, password: str, contact_id: str):
        self.repository.update_password(password=password, id=contact_id)
        
    def send_mail(self):
        pass
    
    def update_full_data_contact(self, data: object):

        post_data = {
            "data_alteracao": ContactHelpers().get_date_now(),
            "nome_completo": data.full_name,
            "telefone": data.phone,
            "cpf": data.cpf,
            "rg": data.rg,
            "sexo": data.sexo,
            "logradouro": data.logradouro,
            "numero_residencial": data.number,
            "cep": data.cep,
            "ponto_referencia": data.reference           
        }
        contact_id = self.repository.get_id_by_contact_email(self.email)
        
        if contact_id:
            self.repository.update_all_data_contact(contact_data=post_data, contact_id=contact_id)
        
        else:
            raise Exception("O usuário não foi encontrado.")
