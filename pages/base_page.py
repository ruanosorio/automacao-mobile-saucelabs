from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

class BasePage:
    def __init__(self, driver, timeout=20):
        self.driver = driver
        self.wait = WebDriverWait(driver, timeout)

    def find(self, locator):
        return self.wait.until(EC.presence_of_element_located(locator))

    def click(self, locator):
        el = self.find(locator)
        el.click()

    def send_keys(self, locator, text):
        el = self.find(locator)
        el.clear()
        el.send_keys(text)
