from http import HTTPStatus
import uuid
import hashlib
import random
import string
from factory.models import User

class CreateUserCore:
    """
    Classe reponsavel por tratar informações referentes ao usuários
    """

    @staticmethod
    def create_id_to_client() -> str:
        """Função responsável por criar novo id para o usuário

        Return:
            str: novo hash id.
        """

        new_id = uuid.uuid4()

        return new_id

    @staticmethod
    def encrypt_password(password: str) -> str:
        
        convert_password = password.encode('ascii')
        encrypt_password = hashlib.md5(convert_password).hexdigest()

        return encrypt_password
    
    
class UpdateUserCore:
    """
    Classe para realizar updates relacionados com o usuário.
    """

    def __init__(self, email_user: str) -> None:
        self.mail = email_user
        self.create_user = CreateUserCore
        self.user_models = User(email_user)

    def new_password_generator(self) -> int:
        """
        Irá gerar uma nova senha para o usuário.

        Return:
            int: status code.
        """

        characters = list(string.ascii_letters + string.digits)

        try:
            random.shuffle(characters)

            password = []
            for i in range(8):
                password.append(random.choice(characters))

            random.shuffle(password)
            new_password = "".join(password)

            print(f"SENHA GERADA: {new_password}")
            # TODO: com o bd criado, salvar no banco e envia por email a nova senha. 
            
            encrypt_password = self.create_user.encrypt_password(new_password)
            
            self.user_models.update_username(encrypt_password)
              
            return HTTPStatus.CREATED

        except:

            return HTTPStatus.INTERNAL_SERVER_ERROR
