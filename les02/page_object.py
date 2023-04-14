from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

class LoginPage:
    def __init__(self, driver):
        self.driver = driver
        self.username_input = (By.NAME, "username")
        self.password_input = (By.NAME, "password")
        self.login_button = (By.CSS_SELECTOR, "button[type='submit']")

    def enter_username(self, username):
        WebDriverWait(self.driver, 10).until(EC.visibility_of_element_located(self.username_input)).send_keys(username)

    def enter_password(self, password):
        WebDriverWait(self.driver, 10).until(EC.visibility_of_element_located(self.password_input)).send_keys(password)

    def click_login_button(self):
        WebDriverWait(self.driver, 10).until(EC.element_to_be_clickable(self.login_button)).click()

class HomePage:
    def __init__(self, driver):
        self.driver = driver
        self.logout_button = (By.CSS_SELECTOR, "button[type='button']")

    def is_logout_button_displayed(self):
        return WebDriverWait(self.driver, 10).until(EC.visibility_of_element_located(self.logout_button)).is_displayed()

def test_login_and_logout(driver):
    login_page = LoginPage(driver)
    login_page.enter_username("username")
    login_page.enter_password("password")
    login_page.click_login_button()

    home_page = HomePage(driver)
    assert home_page.is_logout_button_displayed()

