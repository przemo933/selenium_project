from test_case import TestCase
from selenium.webdriver.common.by import By
from requests import get


# test sprawdza ile jest uszkodzonych obrazków na stronie
class TestBrokenImage(TestCase):
    def test_broken_image(self):
        self.driver.get("http://the-internet.herokuapp.com/broken_images")
        images = self.driver.find_elements(By.TAG_NAME, "img")
        counter = 0
        for image in images:
            response = get(image.get_attribute('src'), stream=True)
            if response.status_code != 200:
                print(image.get_attribute('outerHTML') + " is broken.")
                counter += 1

        print('The page has ' + str(counter) + ' broken images')
