from pages.login_page import LoginPage
from pages.home_page import HomePage
from pages.products_page import ProductPage
from pages.cart_page import CartPage
from pages.checkout_page import CheckoutPage

class PageFactory:
    def __init__(self, driver):
        self.driver = driver

    def login(self):
        return LoginPage(self.driver)

    def home(self):
        return HomePage(self.driver)

    def product(self):
        return ProductPage(self.driver)

    def cart(self):
        return CartPage(self.driver)

    def checkout(self):
        return CheckoutPage(self.driver)