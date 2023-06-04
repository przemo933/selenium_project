import requests as requests

from test_case import TestCase
from selenium.webdriver.common.by import By
import os
import time


class TestFileDownload(TestCase):
    def test_file_download(self):
        self.driver.get("http://the-internet.herokuapp.com/download")

        #pobieranie przykladowego pliku ze strony
        try:
            gotit = self.driver.find_element(By.CSS_SELECTOR, '.example > a:nth-child(26)')
            gotit.click()
            time.sleep(3)
        except Exception:
            self.fail("File's name in not found")

    def test_file_download_2(self):
        self.driver.get("http://the-internet.herokuapp.com/download")

        #pobieranie przykladowego pliku ze strony