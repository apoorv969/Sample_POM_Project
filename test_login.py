import sys
import os
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))

from Pages.LoginPage import LoginPage
from utils.screenshot import take_screenshot

import unittest
from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager
from LoginAutomation.Pages.LoginPage import LoginPage
from LoginAutomation.utils.screenshot import take_screenshot
import HtmlTestRunner
import time

class LoginTest(unittest.TestCase):

    @classmethod
    def setUpClass(cls):
        cls.driver = webdriver.Chrome(service=Service(ChromeDriverManager().install()))
        cls.driver.get("https://practicetestautomation.com/practice-test-login/")
        cls.driver.maximize_window()

    def test_valid_login(self):
        login_page = LoginPage(self.driver)
        login_page.enter_username("student")
        login_page.enter_password("Password123")
        login_page.click_login()
        time.sleep(2)
        self.assertIn("practicetestautomation.com", self.driver.current_url)

    def test_invalid_login(self):
        self.driver.get("https://practicetestautomation.com/practice-test-login/")
        login_page = LoginPage(self.driver)
        login_page.enter_username("wronguser")
        login_page.enter_password("wrongpass")
        login_page.click_login()
        time.sleep(2)
        error_msg = self.driver.find_element("xpath", "//div[@id='error']").text
        self.assertIn("Your username is invalid!", error_msg)

    @classmethod
    def tearDownClass(cls):
        take_screenshot(cls.driver, "final_state")
        cls.driver.quit()

if __name__ == '__main__':
    unittest.main(testRunner=HtmlTestRunner.HTMLTestRunner(output='Reports'))

