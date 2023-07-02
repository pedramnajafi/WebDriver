
from webdriver_manager.chrome import ChromeDriverManager
from selenium import webdriver
driver = webdriver.Chrome(executable_path=ChromeDriverManager().install())
driver.get("http://www.google.com/")
print(driver.title)
driver.quit()


