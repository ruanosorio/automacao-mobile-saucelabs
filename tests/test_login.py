import pytest
import allure
from appium.webdriver.common.appiumby import AppiumBy
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from pages.login_page import LoginPage
from factories.user_factory import UserFactory
from conftest import take_screenshot

LOGIN_TIMEOUT = 20
CART_LOCATOR = (AppiumBy.ACCESSIBILITY_ID, "test-Cart")

@allure.epic("Autenticação")
@allure.feature("Login")
class TestLogin:
    """
    Testes de login com diferentes tipos de usuários.
    """
    def _executar_login(self, driver, user_data, tipo_usuario: str):
        """Executa o fluxo completo de login e valida redirecionamento."""
        lp = LoginPage(driver)

        take_screenshot(driver, f"login_{tipo_usuario}_inicial")

        with allure.step(f"Login com usuário {tipo_usuario}"):
            lp.login(user_data["username"], user_data["password"])
            take_screenshot(driver, f"apos_login_{tipo_usuario}")

        with allure.step("Validar redirecionamento para tela de produtos"):
            wait = WebDriverWait(driver, LOGIN_TIMEOUT)

            try:
                wait.until(EC.presence_of_element_located(CART_LOCATOR))
                take_screenshot(driver, f"login_{tipo_usuario}_sucesso")

            except Exception as e:
                take_screenshot(driver, f"login_{tipo_usuario}_erro")
                allure.attach(
                    str(e), name=f"Erro login {tipo_usuario}",
                    attachment_type=allure.attachment_type.TEXT
                )
                raise AssertionError(f"Falha no login do usuário {tipo_usuario}")

    @allure.story("Login com usuário padrão")
    @allure.severity(allure.severity_level.CRITICAL)
    @pytest.mark.android
    def test_login_standard_user(self, driver):
        """Usuário padrão realiza login com sucesso."""
        user = UserFactory.standard_user()
        self._executar_login(driver, user, "standard_user")

    @allure.story("Login com usuário com problemas")
    @allure.severity(allure.severity_level.NORMAL)
    @pytest.mark.android
    def test_login_problem_user(self, driver):
        """Usuário com problemas realiza login (com possíveis falhas visuais)."""
        user = UserFactory.problem_user()
        self._executar_login(driver, user, "problem_user")
