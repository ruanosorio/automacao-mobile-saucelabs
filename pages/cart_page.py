from appium.webdriver.common.appiumby import AppiumBy
from pages.base_page import BasePage

class CartPage(BasePage):
    def __init__(self, driver):
        super().__init__(driver)
        # Botão de checkout
        self.checkout_button = (AppiumBy.ACCESSIBILITY_ID, "test-CHECKOUT")
        # Título do produto no carrinho
        self.product_name = (AppiumBy.XPATH, "//android.widget.TextView[@text='Sauce Labs Backpack']")

    def proceed_to_checkout(self):
        """Avança para o checkout"""
        self.click(self.checkout_button)

    def verify_product_in_cart(self):
        """Valida se o produto correto está no carrinho"""
        return self.find(self.product_name).is_displayed()
