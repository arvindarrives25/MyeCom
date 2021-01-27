from Configurations.config import TestData
from pageobjects.homepage import HomePage
from pageobjects.loginpage import LoginPage
from testcases.test_base import TestBase


class TestHomePage(TestBase):
    log = TestBase.get_logger()

    """Test case to verify Home page Title"""

    def test_home_page_title(self):
        self.lp = LoginPage(self.driver)
        hp = self.lp.do_login(TestData.USER_NAME, TestData.PASSWORD)
        act_home_page_title = hp.get_home_page_title(TestData.EXP_HP_TITLE)
        if act_home_page_title == TestData.EXP_HP_TITLE:
            self.log.info("Expected title is same as Actual Title, hence test case passed")
            assert True
        else:
            self.log.error("Expected title is not same to Expected Title, hence test case Failed")
            assert False

    """Test case to verify logged in user Name"""

    def test_home_page_logged_user(self):
        self.hp = HomePage(self.driver)
        act_home_page_logged_user_name = self.hp.get_hp_logged_in_user()
        if act_home_page_logged_user_name == TestData.EXP_HP_LOGGED_USER_NAME:
            self.log.info("Expected logged in user is same as Actual logged in user, hence passed")
            assert True
        else:
            self.log.error("Expected logged in user not equals to Actual logged in user, hence Failed")
            assert False

    """Test case to verify if logout link is present"""

    def test_home_page_logout_link(self):
        self.hp = HomePage(self.driver)
        act_home_page_logout_link = self.hp.get_logout_link()
        if act_home_page_logout_link is True:
            self.log.info("Logout link is present , hence Test case passed")
            assert True
        else:
            self.log.error("Logout link is not visible , hence Test case Failed")
            assert False

