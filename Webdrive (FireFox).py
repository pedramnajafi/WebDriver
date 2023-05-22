from webdriver_manager.firefox import GeckoDriverManager
from selenium import webdriver
driver = webdriver.Firefox(executable_path=GeckoDriverManager().install())
driver.get("http://www.google.com/")
print(driver.title)
driver.quit()


