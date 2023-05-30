from selenium import webdriver

driver = webdriver.Chrome()

title = driver.title

driver.get("http://the-internet.herokuapp.com/login")
driver.implicitly_wait(5.5)