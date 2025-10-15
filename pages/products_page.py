from appium.webdriver.common.appiumby import AppiumBy
from pages.base_page import BasePage

class ProductsPage(BasePage):
    def __init__(self, driver):
        super().__init__(driver)
        # Seletor para botão "Add to Cart"
        self.add_to_cart_button = (AppiumBy.ANDROID_UIAUTOMATOR,'new UiSelector().text("ADD TO CART").instance(0)')
        # Ícone do carrinho
        self.cart_icon = (AppiumBy.ACCESSIBILITY_ID, "test-Cart")

    def add_product_to_cart(self):
        """Adiciona o primeiro produto visível ao carrinho"""
        self.click(self.add_to_cart_button)

    def go_to_cart(self):
        """Abre a tela do carrinho"""
        self.click(self.cart_icon)
