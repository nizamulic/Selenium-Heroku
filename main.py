import os
from selenium import webdriver
from selenium.webdriver.common.by import By

chrome_options = webdriver.ChromeOptions()
chrome_options.binary_location = os.environ.get("GOOGLE_CHROME_BIN")
chrome_options.add_argument("--headless")
chrome_options.add_argument("--disable-dev-shm-usage")
chrome_options.add_argument("--no-sandbox")
driver = webdriver.Chrome(os.environ.get("CHROMEDRIVER_PATH"), options=chrome_options)
driver.get("http://139.144.20.91:9000")
print(driver.title)
#driver find all element with a tag
elems = driver.find_elements(By.XPATH, "//a[@href]")
for elem in elems:
    print(elem.get_attribute("href"))
