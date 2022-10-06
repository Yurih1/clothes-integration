from factory.repository import UserRepository


class User:
    """
    Classe resposável por modelas algumas informações do usuario.
    """
    
    def __init__(self, mail: str) -> None:

        self.repository = UserRepository(mail)
        self.email = mail
    
    def get_user_by_mail(self) -> str:
        """Obtem a senha do contato e envia via email.

        Returns:
            str: Nome do usuario vinculado ao e-mail.
        """
        if self.email:
            user = self.repository.get_user()
            return user
        
        else:
            return "Email não informado."
        
    def update_username(self, password: str):
        self.repository.update_username(email=self.email, password=password)
        
    def send_mail(self):
        pass
        