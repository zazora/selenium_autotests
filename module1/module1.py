import math
import os
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait, Select
from selenium.webdriver.support import expected_conditions as EC
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.chrome.service import Service

service = Service(ChromeDriverManager().install())
browser = webdriver.Chrome(service=service)

# calculation
def calc(x):
    return str(math.log(abs(12 * math.sin(int(x)))))

def res(x, y):
    return int(x) + int(y)

# test 1
def test_explicit_wait2():
    url = "http://suninjuly.github.io/explicit_wait2.html"
    browser.get(url)
    
    WebDriverWait(browser, 12).until(EC.text_to_be_present_in_element((By.ID, "price"), "100"))
    browser.find_element(By.ID, "book").click()
    
    num = browser.find_element(By.ID, "input_value").text
    result = calc(num)
    browser.find_element(By.ID, "answer").send_keys(result)
    browser.find_element(By.ID, "solve").click()
    
    alert = browser.switch_to.alert
    print("Test 1 Result:", alert.text.split()[-1])
    alert.accept()

# test 2
def test_get_attribute():
    url = "http://suninjuly.github.io/get_attribute.html"
    browser.get(url)
    
    treasure = WebDriverWait(browser, 12).until(EC.presence_of_element_located((By.ID, "treasure")))
    x = treasure.get_attribute("valuex")
    result = calc(x)
    browser.find_element(By.ID, "answer").send_keys(result)
    
    browser.find_element(By.ID, "robotCheckbox").click()
    browser.find_element(By.ID, "robotsRule").click()
    browser.find_element(By.CLASS_NAME, "btn").click()
    
    alert = browser.switch_to.alert
    print("Test 2 Result:", alert.text.split()[-1])
    alert.accept()

# test 3
def test_selects1():
    url = "http://suninjuly.github.io/selects1.html"
    browser.get(url)
    
    num1 = browser.find_element(By.ID, "num1").text
    num2 = browser.find_element(By.ID, "num2").text
    total = res(num1, num2)
    
    select = Select(browser.find_element(By.ID, "dropdown"))
    select.select_by_visible_text(str(total))
    browser.find_element(By.CLASS_NAME, "btn").click()
    
    alert = browser.switch_to.alert
    print("Test 3 Result:", alert.text.split()[-1])
    alert.accept()

# test 4
def test_execute_script():
    url = "http://suninjuly.github.io/execute_script.html"
    browser.get(url)
    
    num = browser.find_element(By.ID, "input_value").text
    result = calc(num)
    browser.find_element(By.ID, "answer").send_keys(result)
    
    checkbox = browser.find_element(By.ID, "robotCheckbox")
    checkbox.click()
    
    radiobutton = browser.find_element(By.ID, "robotsRule")
    browser.execute_script("arguments[0].scrollIntoView(true);", radiobutton)
    radiobutton.click()
    
    browser.find_element(By.CLASS_NAME, "btn").click()
    
    alert = browser.switch_to.alert
    print("Test 4 Result:", alert.text.split()[-1])
    alert.accept()

# test 5
def test_file_input():
    url = "http://suninjuly.github.io/file_input.html"
    browser.get(url)
    
    browser.find_element(By.NAME, "firstname").send_keys("Ivan")
    browser.find_element(By.NAME, "lastname").send_keys("Ivanov")
    browser.find_element(By.NAME, "email").send_keys("email@ya.ru")
    
    current_dir = os.path.abspath(os.path.dirname(__file__))
    file_path = os.path.join(current_dir, "testFile.txt")
    browser.find_element(By.ID, "file").send_keys(file_path)
    
    browser.find_element(By.CLASS_NAME, "btn").click()
    
    alert = browser.switch_to.alert
    print("Test 5 Result:", alert.text.split()[-1])
    alert.accept()

# test 6
def test_alert_accept():
    url = "http://suninjuly.github.io/alert_accept.html"
    browser.get(url)
    
    browser.find_element(By.CLASS_NAME, "btn").click()
    browser.switch_to.alert.accept()
    
    num = browser.find_element(By.ID, "input_value").text
    result = calc(num)
    browser.find_element(By.ID, "answer").send_keys(result)
    
    browser.find_element(By.CLASS_NAME, "btn").click()
    
    alert = browser.switch_to.alert
    print("Test 6 Result:", alert.text.split()[-1])
    alert.accept()

# test 7
def test_redirect_accept():
    url = "http://suninjuly.github.io/redirect_accept.html"
    browser.get(url)
    
    browser.find_element(By.CLASS_NAME, "btn").click()
    new_window = browser.window_handles[1]
    browser.switch_to.window(new_window)
    
    num = browser.find_element(By.ID, "input_value").text
    result = calc(num)
    browser.find_element(By.ID, "answer").send_keys(result)
    
    browser.find_element(By.CLASS_NAME, "btn").click()
    
    alert = browser.switch_to.alert
    print("Test 7 Result:", alert.text.split()[-1])
    alert.accept()

try:
    test_explicit_wait2()
    test_get_attribute()
    test_selects1()
    test_execute_script()
    test_file_input()
    test_alert_accept()
    test_redirect_accept()
finally:
    browser.quit()
