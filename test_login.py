from test_case import TestCase
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By

class TestLogin(TestCase):

    VALID_LOGIN = "tomsmith"
    VALID_PASSWORD = "SuperSecretPassword!"
    INVALID_LOGIN = "przemek"
    INVALID_PASSWORD = "haslo"

    def test_valid_login(self):
        self.driver.get("http://the-internet.herokuapp.com/login")
        try:
            username_field = self.driver.find_element(By.ID, "username")
        except Exception:
            self.fail("Field not found!")
        username_field.click()
        username_field.send_keys(self.VALID_LOGIN)

        try:
            password_field = self.driver.find_element(By.ID, "password")
        except Exception:
            self.fail("Field not found!")
        password_field.click()
        password_field.send_keys(self.VALID_PASSWORD)

        try:
            login_button = self.driver.find_element(By.XPATH, "/html/body/div[2]/div/div/form/button/i")
        except Exception:
            self.fail("Button not found!")
        login_button.click()

    def test_invalid_login(self):
        self.driver.get("http://the-internet.herokuapp.com/login")
        try:
            username_field = self.driver.find_element(By.ID, "username")
        except Exception:
            self.fail("Field not found!")
        username_field.click()
        username_field.send_keys(self.INVALID_LOGIN)

        try:
            password_field = self.driver.find_element(By.ID, "password")
        except Exception:
            self.fail("Field not found!")
        password_field.click()
        password_field.send_keys(self.INVALID_PASSWORD)

        try:
            login_button = self.driver.find_element(By.XPATH, "/html/body/div[2]/div/div/form/button/i")
        except Exception:
            self.fail("Button not found!")
        login_button.click()



