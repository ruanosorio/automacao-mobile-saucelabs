from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

def wait_for_element(driver, locator, timeout=20):
    return WebDriverWait(driver, timeout).until(EC.presence_of_element_located(locator))

def wait_for_clickable(driver, locator, timeout=20):
    return WebDriverWait(driver, timeout).until(EC.element_to_be_clickable(locator))

def scroll_to_bottom(driver):
    """
    Faz scroll até o final da página usando swipe (iOS e Android).
    Compatível com diferentes tamanhos de tela.
    """
    try:
        # Método usando swipe para scroll
        size = driver.get_window_size()
        start_x = size['width'] // 2
        start_y = int(size['height'] * 0.8)
        end_y = int(size['height'] * 0.2)
        
        driver.swipe(start_x, start_y, start_x, end_y, 500)
    except Exception as e:
        print(f"Erro ao fazer scroll: {e}")