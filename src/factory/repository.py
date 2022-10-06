class UserRepository:
    
    def __init__(self, mail: str) -> None:
        self.email = mail
        
    def get_user(self) -> dict:
        pass
    
    def update_username(self, email: str, password: str) -> None:
        qs = f"""
            UPDATE usuario
            SET password = '{password}'
            WHERE email = '{email}';
        """
        
        #TODO: execute qs.