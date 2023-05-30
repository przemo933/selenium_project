from test_case import TestCase
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By

class TestLogin(TestCase):

    def test_login(self):
        self.driver.get("http://the-internet.herokuapp.com/login")
        try:
            username_field = self.driver.find_element(By.ID, "username")
        except Exception:
            self.fail("Field not found!")
        username_field.click()




