from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

class PageElement(object):
    def __init__(self, browser, timeout=10):
        self.browser = browser
        self.timeout = timeout

    def wait_until_visible(self, locator):
        WebDriverWait(self.browser, self.timeout).until(EC.visibility_of_element_located(locator))

    def wait_until_clickable(self, locator):
        WebDriverWait(self.browser, self.timeout).until(EC.element_to_be_clickable(locator))

    def get_text(self, locator):
        self.wait_until_visible(locator)
        return self.browser.find_element(*locator).text

    def get_attribute(self, locator, attribute):
        self.wait_until_visible(locator)
        return self.browser.find_element(*locator).get_attribute(attribute)

    def is_displayed(self, locator):
        try:
            self.wait_until_visible(locator)
            return True
        except:
            return False

    def is_enabled(self, locator):
        self.wait_until_visible(locator)
        return self.browser.find_element(*locator).is_enabled()

    def click(self, locator):
        self.wait_until_clickable(locator)
        self.browser.find_element(*locator).click()

    def send_keys(self, locator, value):
        self.wait_until_visible(locator)
        self.browser.find_element(*locator).send_keys(value)

