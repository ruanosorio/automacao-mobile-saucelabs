from appium.webdriver.common.appiumby import AppiumBy
from pages.base_page import BasePage

class FinishPage(BasePage):
    def __init__(self, driver):
        super().__init__(driver)
        self.success_message = (AppiumBy.XPATH, "//android.widget.TextView[@text='THANK YOU FOR YOU ORDER']")

    def is_purchase_successful(self):
        """Verifica se a compra foi finalizada com sucesso"""
        return len(self.driver.find_elements(*self.success_message)) > 0
