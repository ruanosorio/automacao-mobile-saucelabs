import json
import os

class CredentialsLoader:
    """Carrega credenciais do arquivo credentials.json"""
    
    def __init__(self, credentials_file="config/credentials.json"):
        self.credentials_file = credentials_file
        self._credentials = None
    
    def _load_credentials(self):
        """Carrega as credenciais do arquivo JSON"""
        if self._credentials is None:
            try:
                current_dir = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
                credentials_path = os.path.join(current_dir, self.credentials_file)
                
                with open(credentials_path, 'r', encoding='utf-8') as file:
                    self._credentials = json.load(file)
            except FileNotFoundError:
                raise FileNotFoundError(f"Arquivo de credenciais não encontrado: {self.credentials_file}")
            except json.JSONDecodeError:
                raise ValueError(f"Erro ao decodificar o arquivo JSON: {self.credentials_file}")
        
        return self._credentials
    
    def get_user_credentials(self, user_type="standard_user"):
        """Obtém todas as credenciais de um usuário"""
        credentials = self._load_credentials()
        
        if user_type not in credentials:
            raise KeyError(f"Usuário '{user_type}' não encontrado nas credenciais")
        
        return credentials[user_type]
    
    def get_user_login_data(self, user_type="standard_user"):
        """Obtém apenas os dados de login (username e password)"""
        user_data = self.get_user_credentials(user_type)
        return {
            "username": user_data["username"],
            "password": user_data["password"]
        }
    
    def get_user_checkout_data(self, user_type="standard_user"):
        """Obtém os dados para checkout (first_name, last_name, postal_code)"""
        user_data = self.get_user_credentials(user_type)
        return {
            "first_name": user_data["first_name"],
            "last_name": user_data["last_name"],
            "postal_code": user_data["postal_code"]
        }