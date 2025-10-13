import pytest
import allure
from factories.user_factory import UserFactory
from pages.login_page import LoginPage
from pages.products_page import ProductsPage
from pages.cart_page import CartPage
from pages.checkout_page import CheckoutPage
from pages.finish_page import FinishPage
from conftest import take_screenshot

@allure.epic("E-commerce")
@allure.feature("Fluxo de Compra")
@allure.story("Compra completa de produto")
@allure.severity(allure.severity_level.CRITICAL)
@pytest.mark.usefixtures("driver")
class TestHiringProducts:

    def test_hiring_products_sucess(self, driver):
        """
        Cenário: Usuário realiza login, adiciona produto ao carrinho,
        realiza o checkout e finaliza a compra com sucesso.

        """
        
        # Screenshot inicial
        take_screenshot(driver, "fluxo_compra_inicial")
        
        with allure.step("Preparar dados de teste"):
            user = UserFactory.standard_user()

        with allure.step("Realizar login"):
            login_page = LoginPage(driver)
            login_page.login(user["username"], user["password"])
            take_screenshot(driver, "apos_login_fluxo")

        with allure.step("Adicionar produto ao carrinho"):
            # Adicionar produto e ir para o carrinho
            products_page = ProductsPage(driver)
            products_page.add_product_to_cart()
            products_page.go_to_cart()

        with allure.step("Confirmar produto no carrinho"):
            cart_page = CartPage(driver)
            assert cart_page.verify_product_in_cart(), "Produto não encontrado no carrinho"
            take_screenshot(driver, "produto_no_carrinho")
            cart_page.proceed_to_checkout()
            take_screenshot(driver, "checkout_iniciado")

        with allure.step("Preencher informações de checkout"):
            checkout_page = CheckoutPage(driver)
            checkout_page.fill_checkout_info_from_credentials()
            take_screenshot(driver, "checkout_preenchido")
            checkout_page.finish_purchase()

        with allure.step("Validar compra finalizada"):
            finish_page = FinishPage(driver)
            take_screenshot(driver, "compra_finalizada")
            
            try:
                assert finish_page.is_purchase_successful(), "A mensagem de sucesso não foi exibida!"
                take_screenshot(driver, "compra_sucesso")
            except AssertionError:
                take_screenshot(driver, "compra_erro")
                raise