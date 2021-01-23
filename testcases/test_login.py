from Configurations.config import TestData
from pageobjects.loginpage import LoginPage
from testcases.test_base import TestBase


class TestLogin(TestBase):

    def test_do_login(self):
        self.loginpage = LoginPage(self.driver)
        self.loginpage.do_login(TestData.USER_NAME, TestData.PASSWORD)