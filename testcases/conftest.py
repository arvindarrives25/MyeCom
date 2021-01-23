import pytest
from selenium import webdriver
from selenium.common.exceptions import TimeoutException, NoSuchElementException

from Configurations.config import TestData


@pytest.fixture(params=["chrome"], scope="class")
def init_driver(request):
    request.param == "chrome"
    web_driver = webdriver.Chrome(executable_path="D:\\Drivers_For_Testing\\chromedriver_win32\\chromedriver.exe")
    request.cls.driver = web_driver
    try:
        web_driver.get(TestData.BASE_URL)
    except Exception as e:
        print(e)
        pass
    web_driver.maximize_window()
    yield
    web_driver.close()
