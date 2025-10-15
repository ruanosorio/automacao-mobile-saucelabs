from appium.webdriver.common.appiumby import AppiumBy
from pages.base_page import BasePage
from utils.credentials_loader import CredentialsLoader
from utils.helpers import scroll_to_bottom

class CheckoutPage(BasePage):
    """
    Page Object da tela de Checkout.
    Responsável por preencher dados do usuário e finalizar a compra.
    """

    def __init__(self, driver):
        super().__init__(driver)
        self.credentials_loader = CredentialsLoader()

        # Locators
        self.first_name_field = (AppiumBy.ACCESSIBILITY_ID, "test-First Name")
        self.last_name_field = (AppiumBy.ACCESSIBILITY_ID, "test-Last Name")
        self.zip_field = (AppiumBy.ACCESSIBILITY_ID, "test-Zip/Postal Code")
        self.continue_button = (AppiumBy.ACCESSIBILITY_ID, "test-CONTINUE")
        self.finish_button = (AppiumBy.ACCESSIBILITY_ID, "test-FINISH")

    def fill_checkout_info(self, first_name: str, last_name: str, zip_code: str):
        """
        Preenche manualmente as informações do checkout.
        Args:
            first_name (str): Primeiro nome
            last_name (str): Último nome
            zip_code (str): Código postal
        """
        self.send_keys(self.first_name_field, first_name)
        self.send_keys(self.last_name_field, last_name)
        self.send_keys(self.zip_field, zip_code)
        self.click(self.continue_button)

    def fill_checkout_info_from_credentials(self, user_type: str = "standard_user"):
        """
        Preenche automaticamente as informações de checkout com base
        nos dados do arquivo credentials.json.
        """
        checkout_data = self.credentials_loader.get_user_checkout_data(user_type)
        self.fill_checkout_info(
            checkout_data["first_name"],
            checkout_data["last_name"],
            checkout_data["postal_code"]
        )

    def finish_purchase(self):
        """
        Faz scroll até o final da página e finaliza a compra clicando no botão 'FINISH'.
        """
        scroll_to_bottom(self.driver)
        
        # Finaliza a compra
        self.click(self.finish_button)
