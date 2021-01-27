from Configurations.config import TestData
from pageobjects.loginpage import LoginPage
from testcases.test_base import TestBase


class TestLogin(TestBase):

    log = TestBase.get_logger()

    """Test case for login page title"""
    def test_login_page_title(self):
        self.lp = LoginPage(self.driver)
        act_login_page_title = self.lp.get_login_page_title(TestData.EXP_LP_TITLE)
        if act_login_page_title == TestData.EXP_LP_TITLE:
            self.log.info("Actual title matches expected title, hence Test case passed")
            assert True
        else:
            self.log.error("Actual title not equals to expected title, hence Test case Failed")
            assert False

    """Test case for login page welcome message"""
    def test_login_page_welcome_message(self):
        self.lp = LoginPage(self.driver)
        act_login_page_welcome_message = self.lp.get_login_page_welcome_message()
        if act_login_page_welcome_message == TestData.EXP_LP_WELCOME_MSG:
            self.log.info("Actual welcome message matches expected welcome message, hence Test case passed")
            assert True
        else:
            self.log.error("Actual welcome message not matches expected welcome message, hence Test case Failed")
            assert False

    """Test case for successful login"""
    def test_do_login(self):
        self.lp = LoginPage(self.driver)
        self.lp.do_login(TestData.USER_NAME, TestData.PASSWORD)

