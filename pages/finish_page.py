from appium.webdriver.common.appiumby import AppiumBy

class FinishPage:
    def __init__(self, driver):
        self.driver = driver
        self.success_message = (AppiumBy.XPATH, "//android.widget.TextView[@text='THANK YOU FOR YOU ORDER']")

    def is_purchase_successful(self):
        return len(self.driver.find_elements(*self.success_message)) > 0
