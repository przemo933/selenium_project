from test_case import TestCase
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By


# noinspection PyBroadException
class TestLoginStore(TestCase):
    VALID_LOGIN = "admin@yourstore.com"
    VALID_PASSWORD = "admin"
    VALID_LOGIN_TITLE = "Dashboard / nopCommerce administration"
    INVALID_LOGIN = "przemek@wp.pl"
    INVALID_PASSWORD = "haslo"

    # funkcja testujaca logowanie z prawidłowymi danymi
    def test_valid_login(self):
        try:
            self.driver.get("https://admin-demo.nopcommerce.com/login")
            username_field = self.driver.find_element(By.ID, "Email")
            username_field.clear()
            username_field.send_keys(self.VALID_LOGIN)
            password_field = self.driver.find_element(By.ID, "Password")
            password_field.clear()
            password_field.send_keys(self.VALID_PASSWORD)
            login_button = self.driver.find_element(By.CSS_SELECTOR, ".button-1")
            login_button.click()
        except Exception:
            self.fail("Login with valid login details failed!")
        print()
        print(8 * "--------")

        # sprawdzamy czy tytuł strony po zalogowaniu jest prawidłowy
        title = self.driver.title
        if title == self.VALID_LOGIN_TITLE:
            print("Title after login matched")
        else:
            print("Invalid title")

    # funkcja testujaca logowanie z nieprawidłowymi danymi
    def test_invalid_login(self):
        try:
            self.driver.get("https://admin-demo.nopcommerce.com/login")
            username_field = self.driver.find_element(By.ID, "Email")
            username_field.clear()
            username_field.send_keys(self.INVALID_LOGIN)
            password_field = self.driver.find_element(By.ID, "Password")
            password_field.clear()
            password_field.send_keys(self.INVALID_PASSWORD)
            login_button = self.driver.find_element(By.CSS_SELECTOR, ".button-1")
            login_button.click()
        except Exception:
            self.fail("Login with valid login details failed!")

        # sprawdza czy na stronie wyświetliła się wiadomośc o błędnym logowaniu
        self.driver.find_element(By.CSS_SELECTOR,
                                 "html.html-login-page body div.master-wrapper-page div.master-wrapper-"
                                 "content div.master-column-wrapper div.center-1 div.page.login-page div"
                                 ".page-body div.customer-blocks div.returning-wrapper.fieldset form div"
                                 ".message-error.validation-summary-errors")
