from selenium.webdriver.common.by import By

from pageobjects.basepage import BasePage


class LoginPage(BasePage):

    __textbox_username = (By.ID, "Email")
    __textbox_password = (By.ID, "Password")
    __button_login = (By.XPATH, "//input[@value='Log in']")

    def __init__(self, driver):
        super().__init__(driver)

    def do_login(self, username, password):
        self.do_send_keys(self.__textbox_username, username)
        self.do_send_keys(self.__textbox_password, password)
        self.do_click(self.__button_login)
