from selenium.webdriver.common.by import By
from pageobjects.basepage import BasePage
from pageobjects.homepage import HomePage


class LoginPage(BasePage):
    __textbox_username = (By.ID, "Email")
    __textbox_password = (By.ID, "Password")
    __button_login = (By.XPATH, "//input[@value='Log in']")
    __txt_welcome_message = (By.CSS_SELECTOR, "div.title > strong")

    def __init__(self, driver):
        super().__init__(driver)

    """This method will return welcome message text of the login page"""
    def get_login_page_welcome_message(self):
        return self.get_text(self.__txt_welcome_message)

    """This method will return the title of the login page"""
    def get_login_page_title(self, title):
        return self.get_title(title)

    """This method will clear and supply username & password, finally will hit login button"""
    def do_login(self, username, password):
        self.do_send_keys(self.__textbox_username, username)
        self.do_send_keys(self.__textbox_password, password)
        self.do_click(self.__button_login)
        return HomePage(self.driver)
