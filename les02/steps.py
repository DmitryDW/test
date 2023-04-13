from selenium import webdriver
from pages.login_page import LoginPage
from pages.home_page import HomePage

class TestLogin:
    def setup_method(self):
        self.browser = webdriver.Chrome()
        self.browser.maximize_window()
        self.browser.implicitly_wait(10)

    def teardown_method(self):
        self.browser.quit()

    def test_login(self):
        login_page = LoginPage(self.browser)
        home_page = HomePage(self.browser)

        login_page.open()
        login_page.enter_username("username")
        login_page.enter_password("password")
        login_page.click_login_button()

        assert home_page.is_logged_in()
