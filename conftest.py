import os
import pytest
from appium import webdriver
from appium.options.android import UiAutomator2Options
from dotenv import load_dotenv

load_dotenv()

@pytest.fixture(scope="function")
def driver():
    appium_server_url = f"http://{os.getenv('APPIUM_HOST')}:{os.getenv('APPIUM_PORT')}"

    options = UiAutomator2Options()
    options.platform_name = "Android"
    options.device_name = os.getenv("DEVICE_NAME")
    options.platform_version = os.getenv("PLATFORM_VERSION")
    options.app = os.path.abspath(os.getenv("APP_PATH"))
    options.app_package = "com.swaglabsmobileapp"
    options.app_activity = ".MainActivity"
    options.auto_grant_permissions = True
    options.new_command_timeout = 300

    driver = webdriver.Remote(appium_server_url, options=options)
    driver.implicitly_wait(10)

    yield driver
    driver.quit()

# Função simples para capturar screenshots
def take_screenshot(driver, step_name):
    """Captura screenshot e anexa ao Allure"""
    try:
        import allure
        from datetime import datetime
        
        timestamp = datetime.now().strftime("%Y%m%d_%H%M%S")
        screenshot_name = f"{step_name}_{timestamp}"
        
        # Captura screenshot
        screenshot_data = driver.get_screenshot_as_png()
        
        # Anexa ao Allure
        allure.attach(
            screenshot_data,
            name=screenshot_name,
            attachment_type=allure.attachment_type.PNG
        )
        
        # Salva arquivo local (opcional)
        screenshots_dir = "screenshots"
        if not os.path.exists(screenshots_dir):
            os.makedirs(screenshots_dir)
        
        filepath = os.path.join(screenshots_dir, f"{screenshot_name}.png")
        with open(filepath, 'wb') as f:
            f.write(screenshot_data)
            
        print(f"📸 Screenshot: {screenshot_name}")
        
    except Exception as e:
        print(f"❌ Erro ao capturar screenshot: {str(e)}")

# Hook para capturar screenshot em falhas
@pytest.hookimpl(tryfirst=True, hookwrapper=True)
def pytest_runtest_makereport(item, call):
    """Hook para capturar resultado do teste"""
    outcome = yield
    rep = outcome.get_result()
    setattr(item, "rep_" + rep.when, rep)

@pytest.fixture(autouse=True)
def screenshot_on_failure(request, driver):
    """Captura screenshot automaticamente em caso de falha"""
    yield
    if hasattr(request.node, 'rep_call') and request.node.rep_call.failed:
        take_screenshot(driver, f"FALHA_{request.node.name}")
