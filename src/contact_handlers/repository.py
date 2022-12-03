class UserRepository:
    
    def __init__(self, email: str) -> None:
        self.email = email
        
    def create_new_contact(self, data: dict):
        query = f"""
            INSERT INTO 
                contato (id, email, password)
                VALUES ({data['id']}, {data['usuario']}, {data['password']})
        """
        
        #TODO: execute query.
    
    def update_password(self, password: str, id: str) -> None:
        query = f"""
            UPDATE 
                contato
            SET 
                password = '{password}'
            WHERE id = '{id}';
        """
        
        #TODO: execute query.
    
    def get_id_by_contact_email(self) -> str:
        query = f"""
            SELECT 
                id
            FROM contato
            WHERE email = '{self.email}'
        """
        
        #TODO: execute query.
        
        return "1234"
        
    def update_all_data_contact(self, contact_data: dict, contact_id):
        query = f"""
            UPDATE 
                contato
            SET 
                data_alteracao = '{contact_data["data_alteracao"]}',
                nome_completo = '{contact_data["nome_completo"]}',
                telefone = '{contact_data["telefone"]}',
                cpf = '{contact_data["cpf"]}',
                rg = '{contact_data["rg"]}',
                sexo = '{contact_data["sexo"]}',
                logradouro = '{contact_data["logradouro"]}',
                numero_residencial = '{contact_data["numero_residencial"]}',
                cep = '{contact_data["cep"]}',
                ponto_referencia = '{contact_data["ponto_referencia"]}'
            WHERE id = '{self.email}';
        """
        
        #TODO: execute query.