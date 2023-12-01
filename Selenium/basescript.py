from selenium import webdriver
from selenium.webdriver.common.by import By
import time

driver = webdriver.Firefox()
driver.get('http://inventwithpython.com')

data = driver.find_element(By.CLASS_NAME, 'display-3')
print(data)
print(data.text)




# time.sleep(100)
# driver.close()