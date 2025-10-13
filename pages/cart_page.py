from appium.webdriver.common.appiumby import AppiumBy

class CartPage:
    def __init__(self, driver):
        self.driver = driver
        # Botão de checkout
        self.checkout_button = (AppiumBy.ACCESSIBILITY_ID, "test-CHECKOUT")
        # Título do produto no carrinho
        self.product_name = (AppiumBy.XPATH, "//android.widget.TextView[@text='Sauce Labs Backpack']")

    def proceed_to_checkout(self):
        """Avança para o checkout"""
        self.driver.find_element(*self.checkout_button).click()

    def verify_product_in_cart(self):
        """Valida se o produto correto está no carrinho"""
        return self.driver.find_element(*self.product_name).is_displayed()
