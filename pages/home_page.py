from appium.webdriver.common.appiumby import AppiumBy
from pages.base_page import BasePage

class HomePage(BasePage):
    FIRST_PRODUCT_ADD = (AppiumBy.ACCESSIBILITY_ID, "test-ADD TO CART")
    CART_ICON = (AppiumBy.ACCESSIBILITY_ID, "test-Cart")

    def add_first_product_to_cart(self):
        """Adiciona o primeiro produto visível ao carrinho"""
        buttons = self.driver.find_elements(*self.FIRST_PRODUCT_ADD)
        if buttons:
            buttons[0].click()
        else:
            raise Exception("Nenhum botão de add encontrado")

    def open_cart(self):
        """Abre a tela do carrinho"""
        self.click(self.CART_ICON)