from test_case import TestCase
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
import time


class TestFileDownload(TestCase):
    def test_file_download(self):
        self.driver.get("http://the-internet.herokuapp.com/download")

        #pobieranie przykladowego pliku ze strony
        try:
            self.driver.find_element(By.CSS_SELECTOR, '.example > a:nth-child(26)').click()
            time.sleep(3)
        except Exception:
            self.fail("File's name in not found")

    def test_file_generate_and_download(self):
        self.driver.get("https://demo.automationtesting.in/FileDownload.html")
        self.driver.maximize_window()

        #generowanie i pobieranie pliku txt
        self.driver.find_element(By.XPATH, '//*[@id="textbox"]').send_keys('testing download text file')
        self.driver.find_element(By.XPATH, '//*[@id="createTxt"]').send_keys(Keys.ENTER)
        self.driver.find_element(By.XPATH, '//*[@id="link-to-download"]').send_keys(Keys.ENTER)
        time.sleep(1)

        # #gererowanie i pobieranie pliku pdf
        self.driver.find_element(By.ID, 'pdfbox').send_keys('testing pdf')
        self.driver.find_element(By.ID, 'createPdf').send_keys(Keys.ENTER)
        self.driver.find_element(By.ID, 'pdf-link-to-download').send_keys(Keys.ENTER)
        time.sleep(1)


