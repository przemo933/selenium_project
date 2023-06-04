import unittest
from selenium import webdriver


class TestCase(unittest.TestCase):
    def setUp(self):
        self.driver = webdriver.Chrome()
    def wait(self):
        self.driver.implicitly_wait(10)
    def tearDown(self):
        self.driver.close()