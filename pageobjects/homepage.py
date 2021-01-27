from selenium.webdriver.common.by import By
from pageobjects.basepage import BasePage


class HomePage(BasePage):

    __txt_hp_logged_in_user = (By.CSS_SELECTOR, "li.account-info")
    __lnk_hp_logout = (By.XPATH, "//*[text()='Logout']")

    def __init__(self, driver):
        super().__init__(driver)

    """This method will return the title of the Home page"""
    def get_home_page_title(self, title):
        return self.get_title(title)

    """This method will return text of the logged in user of Home page"""
    def get_hp_logged_in_user(self):
        return self.get_text(self.__txt_hp_logged_in_user)

    """This method will return if logout link is visible"""
    def get_logout_link(self):
        return self.element_visible(self.__lnk_hp_logout)

