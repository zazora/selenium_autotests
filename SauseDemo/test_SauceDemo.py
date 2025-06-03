import selenium,time
from selenium import webdriver
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.support.ui import Select

service=Service(ChromeDriverManager().install())
browser=webdriver.Chrome(service=service)


url="https://www.saucedemo.com/" 
browser.get(url)

pref=['standard_user','secret_sauce']
selectors=['input[name="user-name"]','input[name="password"]']

for i in range(len(pref)):
	browser.find_element(By.CSS_SELECTOR,selectors[i]).send_keys(pref[i])

button=browser.find_element(By.CSS_SELECTOR,'input[type="submit"]')
button.click()

time.sleep(5)
browser.close()
browser.quit()
