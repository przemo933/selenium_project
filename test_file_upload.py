from test_case import TestCase
from selenium.webdriver.common.by import By
from time import sleep

# noinspection PyBroadException
class TestFileUpload(TestCase):

    # funkcja testujaca upload pliku
    def test_file_upload(self):
        self.driver.get("http://the-internet.herokuapp.com/upload")
        try:
            self.driver.find_element(By.ID, "file-upload").send_keys("/Users/MacBookPro/Git_repos/selenium_project/"
                                                                     "test_files/test.txt")
            self.driver.find_element(By.ID, "file-submit").submit()
            if (self.driver.page_source.find("File Uploaded!")):
                print("file upload success")
            else:
                print("file upload not successful")
        except Exception:
            self.fail("Field not found!")