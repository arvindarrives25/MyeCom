from selenium import webdriver
from selenium.common.exceptions import NoSuchElementException, TimeoutException
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as ec

from Configurations.config import TestData

""" This class is the parent of all the page classes
    It contains all the custom methods(for example, click(), sendKeys() etc.
"""


class BasePage:
    driver: webdriver.Chrome

    def __init__(self, driver):
        self.driver = driver

    """This is a custom click method, which will wait until the element is visible before clicking """
    try:
        def do_click(self, locator):
            WebDriverWait(self.driver, TestData.EXPLICIT_WAIT).until(ec.element_to_be_clickable(locator)).click()
    except NoSuchElementException:
        print("Could not find the clickable element")

    """This method will first clear the input box and then type """
    try:
        def do_send_keys(self, locator, text):
            my_element = WebDriverWait(self.driver, TestData.EXPLICIT_WAIT).until(ec.element_to_be_clickable(locator))
            my_element.click()
            my_element.clear()
            my_element.send_keys(text)
    except TimeoutException as e:
        print("Page load Timeout Occurred. Quiting !!!")

    """This method will return text of the web element"""
    try:
        def get_text(self, locator):
            my_element = WebDriverWait(self.driver, TestData.EXPLICIT_WAIT).until(
                ec.visibility_of_element_located(locator))
            return my_element.text
    except NoSuchElementException:
        print("Could not find the locator of the text")

        """This method will return if the webElement is visible or not!"""
    try:
        def element_visible(self, locator):
            my_element = WebDriverWait(self.driver, TestData.EXPLICIT_WAIT).until(
                ec.visibility_of_element_located(locator))
            return bool(my_element)
    except NoSuchElementException:
        print("WebElement is not visible ")

    """This method will return if the WebElement is enabled or not!"""
    try:
        def element_enabled(self, locator):
            my_element = WebDriverWait(self.driver, TestData.EXPLICIT_WAIT).until(
                ec.visibility_of_element_located(locator))
            return bool(my_element)
    except NoSuchElementException:
        print("WebElement is not enabled")

    """This method will return title of the page"""
    try:
        def get_title(self, title):
            WebDriverWait(self.driver, TestData.EXPLICIT_WAIT).until(ec.title_is(title))
            return self.driver.title
    except NoSuchElementException:
        print("Title is not present")
