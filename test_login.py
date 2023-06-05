from test_case import TestCase
from selenium.webdriver.common.by import By


# noinspection PyBroadException
class TestLogin(TestCase):
    VALID_LOGIN = "tomsmith"
    VALID_PASSWORD = "SuperSecretPassword!"
    INVALID_LOGIN = "przemek"
    INVALID_PASSWORD = "haslo"

    # funkcja testujaca logowanie z prawidłowymi danymi
    def test_valid_login(self):
        self.driver.get("http://the-internet.herokuapp.com/login")
        try:
            username_field = self.driver.find_element(By.ID, "username")
            username_field.click()
            username_field.send_keys(self.VALID_LOGIN)
        except Exception:
            self.fail("Field not found!")

        try:
            password_field = self.driver.find_element(By.ID, "password")
            password_field.click()
            password_field.send_keys(self.VALID_PASSWORD)
        except Exception:
            self.fail("Field not found!")

        try:
            login_button = self.driver.find_element(By.XPATH, "/html/body/div[2]/div/div/form/button/i")
        except Exception:
            self.fail("Button not found!")
        login_button.click()

        # sprawdza czy pojawił sie prawidłowy komunkiat po zalogowaniu poprawnymi danymi
        self.driver.find_element(By.CSS_SELECTOR, "html.no-js body div.row div#flash-messages.large-12.columns div#"
                                                  "flash.flash.success")

    # funkcja testujaca logowanie z nieprawidłowymi danymi
    def test_invalid_login(self):
        self.driver.get("http://the-internet.herokuapp.com/login")
        try:
            username_field = self.driver.find_element(By.ID, "username")
            username_field.click()
            username_field.send_keys(self.INVALID_LOGIN)
        except Exception:
            self.fail("Field not found!")

        try:
            password_field = self.driver.find_element(By.ID, "password")
            password_field.click()
            password_field.send_keys(self.INVALID_PASSWORD)
        except Exception:
            self.fail("Field not found!")

        try:
            login_button = self.driver.find_element(By.XPATH, "/html/body/div[2]/div/div/form/button/i")
        except Exception:
            self.fail("Button not found!")
        login_button.click()

        # sprawdza czy pojawił sie prawidłowy komunikat po zalogowaniu niepoprawnymi danymi
        self.driver.find_element(By.CSS_SELECTOR, "html.no-js body div.row div#flash-messages.large-12.columns div#"
                                                  "flash.flash.error")

