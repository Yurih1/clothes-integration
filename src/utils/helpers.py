import uuid
import hashlib
from datetime import datetime
import pytz
import random
import string


class ContactHelpers:
    
    @staticmethod
    def create_id_to_client() -> str:
        """Função responsável por criar novo id para o usuário

        Return:
            str: novo hash id.
        """

        new_id = uuid.uuid4()

        return str(new_id)

    @staticmethod
    def create_new_password() -> str:
        characters = list(string.ascii_letters + string.digits)

        random.shuffle(characters)

        password = []
        for i in range(8):
            password.append(random.choice(characters))

        random.shuffle(password)
        new_password = "".join(password)
        
        return new_password

    @staticmethod
    def encrypt_password(password: str) -> str:
        
        convert_password = password.encode('ascii')
        encrypt_password = hashlib.md5(convert_password).hexdigest()

        return encrypt_password

    @staticmethod
    def get_date_now() -> str:
        """Obtem a data e hora no fuso horário de Sao paulo.

        Returns:
            str: data e hora.
        """
        now = datetime.now(tz=pytz.timezone("America/Sao_Paulo"))
        date = now.strftime("%d-%m-%Y - %H:%M:%S")
        
        return date
