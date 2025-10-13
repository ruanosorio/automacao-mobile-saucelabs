from utils.credentials_loader import CredentialsLoader

class UserFactory:
    """
    Factory para criar dados de usuários baseados no arquivo credentials.json
    """
    
    def __init__(self):
        self.credentials_loader = CredentialsLoader()
    
    @staticmethod
    def standard_user():
        """
        Retorna dados de login do usuário padrão
        """
        credentials_loader = CredentialsLoader()
        return credentials_loader.get_user_login_data("standard_user")
    
    @staticmethod
    def get_user_data(user_type: str = "standard_user"):
        """
        Retorna todos os dados do usuário especificado
        """
        credentials_loader = CredentialsLoader()
        return credentials_loader.get_user_credentials(user_type)
    
    @staticmethod
    def get_checkout_data(user_type: str = "standard_user"):
        """
        Retorna dados para checkout do usuário especificado
        """
        credentials_loader = CredentialsLoader()
        return credentials_loader.get_user_checkout_data(user_type)


    @staticmethod
    def problem_user():
        """
        Retorna dados de login do usuário problem_user
        """
        credentials_loader = CredentialsLoader()
        return credentials_loader.get_user_login_data("problem_user")