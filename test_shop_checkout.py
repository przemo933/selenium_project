from random import randint
from test_case import TestCase
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from time import sleep
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support.expected_conditions import presence_of_element_located


class TestShopCheckout(TestCase):
    FIRST_NAME = 'Jan'
    LAST_NAME = 'Kowalski'
    COUNTRY = 'Poland'
    STREET_ADDRESS = 'Klonowa 5'
    POSTCODE = '23-232'
    CITY = 'Wroclaw'
    PHONE = '787000999'
    EMAIL = 'test'.join(str(randint(1, 99999))) + '@test.pl'
    USERNAME = 'testing'.join(str(randint(1, 99999)))
    PASSWORD = 'Test123'

    # funkcja testujaca dodanie produktu do koszyka i zrealizowania zamówienia testowymi danymi
    def test_shop_checkout(self):
        self.driver.get("https://practice.automationbro.com/shop")
        self.driver.maximize_window()
        item = self.driver.find_element(By.XPATH, "/html/body/div[1]/main/div/div/div/ul/li[1]/a[2]")
        item.click()
        sleep(2)
        cart = self.driver.find_element(By.XPATH, "/html/body/div[1]/header/div/div/div[2]/div[1]/ul/li[2]/a/i")
        cart.click()
        proceed_xpath = "/html/body/div[1]/main/div/div/div/article/div/div[2]/div[2]/div/div/a"
        proceed = WebDriverWait(self.driver, 10).until(presence_of_element_located((By.XPATH, proceed_xpath)))
        proceed.click()

        self.driver.find_element(By.ID, "billing_first_name").send_keys(self.FIRST_NAME)
        self.driver.find_element(By.ID, "billing_last_name").send_keys(self.LAST_NAME)
        self.driver.find_element(By.ID, "select2-billing_country-container").click()
        self.driver.find_element(By.XPATH, "/html/body/span[2]/span/span[1]/input").send_keys(self.COUNTRY)
        self.driver.find_element(By.XPATH, "/html/body/span[2]/span/span[1]/input").send_keys(Keys.ENTER)
        self.driver.find_element(By.ID, "billing_address_1").send_keys(self.STREET_ADDRESS)
        self.driver.find_element(By.ID, "billing_postcode").send_keys(self.POSTCODE)
        self.driver.find_element(By.ID, "billing_city").send_keys(self.CITY)
        self.driver.find_element(By.ID, "billing_phone").send_keys(self.PHONE)
        self.driver.find_element(By.ID, "billing_email").send_keys(self.EMAIL)
        self.driver.find_element(By.ID, "account_username").send_keys(self.USERNAME)
        self.driver.find_element(By.ID, "account_password").send_keys(self.PASSWORD)
        self.driver.find_element(By.ID, "place_order").click()
        sleep(6)
        self.driver.save_screenshot("image.png")
