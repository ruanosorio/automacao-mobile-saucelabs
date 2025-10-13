from appium.webdriver.common.appiumby import AppiumBy

class ProductsPage:
    def __init__(self, driver):
        self.driver = driver

        # Seletor para botão "Add to Cart"
        self.add_to_cart_button = (AppiumBy.ANDROID_UIAUTOMATOR,'new UiSelector().text("ADD TO CART").instance(0)')

        # Ícone do carrinho
        self.cart_icon = (AppiumBy.ACCESSIBILITY_ID, "test-Cart")

    def add_product_to_cart(self):
        """Adiciona o primeiro produto visível ao carrinho"""
        self.driver.find_element(*self.add_to_cart_button).click()

    def go_to_cart(self):
        """Abre a tela do carrinho"""
        self.driver.find_element(*self.cart_icon).click()
