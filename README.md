# WebDriver
Selenium WebDriver is a popular web-based automation testing framework that is primarily used for automating tasks related to Web UI testing.
Selenium WebDriver is the main component that communicates with the web browser.

Google Chrome:

      from webdriver_manager.chrome import ChromeDriverManager
      from selenium import webdriver
      driver = webdriver.Chrome(executable_path=ChromeDriverManager().install())
      driver.get("http://www.google.com/")
      print(driver.title)
      driver.quit()


ّFireFox:

      from webdriver_manager.firefox import GeckoDriverManager
      from selenium import webdriver
      driver = webdriver.Firefox(executable_path=GeckoDriverManager().install())
      driver.get("http://www.google.com/")
      print(driver.title)
      driver.quit()


