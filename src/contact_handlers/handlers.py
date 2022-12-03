from contact_handlers.models import User
from utils.helpers import ContactHelpers
from http import HTTPStatus


class CreateUserHandlers:
    """
    Classe reponsavel por criar novo contato.
    """
    def __init__(self, email_user) -> None:
        self.helpers = ContactHelpers()
        self.user_models = User(email_user)
    
    def create_contact(self, data: object) -> bool:
        id_generated = self.helpers.create_id_to_client()
        
        create_hash_pass = self.helpers.encrypt_password(data.password)
        
        data_contact = {
            "id": id_generated,
            "usuario": data.username,
            "password": create_hash_pass
        }
        self.user_models.post_new_contact(post_data=data_contact)
        
        #TODO: fazer uma validação
        return True


class UpdateUserHandlers:
    """
    Classe para realizar updates relacionados com o usuário.
    """

    def __init__(self, email_user: str) -> None:
        self.email = email_user
        self.user_models = User(email_user)
        self.helpers = ContactHelpers()

    def new_password_generator(self) -> int:
        """
        Irá gerar uma nova senha para o usuário.

        Return:
            int: status code.
        """

        try:

            new_password = self.helpers.create_new_password()
            
            encrypt_password = self.helpers.encrypt_password(new_password)
            
            contact_id = self.user_models.get_user_by_email()
            
            self.user_models.update_password(password=encrypt_password, contact_id=contact_id)

            #TODO: envia new_password por email
            return HTTPStatus.CREATED

        except:

            return HTTPStatus.INTERNAL_SERVER_ERROR

    def update_full_data_contact(self, data: object):
        
        if data.email:
            self.user_models.update_full_data_contact(data)
            
            #TODO: cria uma validação
            return True
        
        else:
            raise Exception("O usuário não foi encontrado.")
