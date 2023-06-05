from test_case import TestCase
from selenium.webdriver.common.by import By
from time import sleep


class TestShopCart(TestCase):

    # funkcja testujaca wyszukiwanie produktu, dodanie do koszyka i usuwanie z koszyka
    def test_shop_search_add_remove_cart(self):
        self.driver.get("https://practice.automationbro.com/shop")
        search_field = self.driver.find_element(By.ID, "woocommerce-product-search-field-0")
        search_field.send_keys("watch")
        add_cart_1 = self.driver.find_element(By.XPATH, "/html/body/div[1]/main/div/div/div/ul/li[1]/a[2]")
        add_cart_1.click()
        add_cart_2 = self.driver.find_element(By.XPATH, "/html/body/div[1]/main/div/div/div/ul/li[2]/a[2]")
        add_cart_2.click()
        sleep(2)
        cart = self.driver.find_element(By.XPATH, "/html/body/div[1]/header/div/div/div[2]/div[1]/ul/li[2]/a/i")
        cart.click()
        # usuwanie pierwszej pozycji z koszyka
        self.driver.find_element(By.XPATH, "/html/body/div[1]/main/div/div/div/article/div/div[2]/form/table/"
                                           "tbody/tr[2]/td[1]/a").click()
        sleep(4)
        # usuwanie drugiej pozycji z koszyka
        self.driver.find_element(By.XPATH, "/html/body/div[1]/main/div/div/div/article/div/div[2]/form/table/"
                                           "tbody/tr[1]/td[1]/a").click()
