from test_case import TestCase
from selenium.webdriver.common.by import By

class TestCheckbox(TestCase):
    WEBSITE = "http://the-internet.herokuapp.com/checkboxes"

    # funkcja sprawdza czy można zaznyczycz pola checkbox (domyślnie odznaczone)
    def test_first_checkbox(self):
        try:
            self.driver.get(self.WEBSITE)
            first_checkbox = self.driver.find_element(By.XPATH, "/html/body/div[2]/div/div/form/input[1]")
            first_checkbox.click()
        except Exception:
            self.fail("Fail to find/select first chceckbox")

        # sprawdza czy zoastał zaznaczony checkbox
        if first_checkbox.is_selected():
            print("Pass select first checkbox")
        else:
            print("Fail")

    # funkcja sprawdza czy można zaznyczycz pola checkbox (domyślnie znaczone)
    def test_second_checkbox(self):
        try:
            self.driver.get(self.WEBSITE)
            first_checkbox = self.driver.find_element(By.XPATH, "/html/body/div[2]/div/div/form/input[2]")
            first_checkbox.click()
        except Exception:
            self.fail("Fail to find/select second chceckbox")

        # sprawdza czy został odznaczony checkbox
        if not first_checkbox.is_selected():
            print("Pass unselect second checkbox")
        else:
            print("Fail")