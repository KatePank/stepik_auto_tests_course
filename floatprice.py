from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.ui import WebDriverWait
import math
import time

browser = webdriver.Chrome()
browser.get('https://suninjuly.github.io/explicit_wait2.html')

price = WebDriverWait(browser, 13).until(EC.text_to_be_present_in_element((By.ID, 'price'), '100'))
book = browser.find_element(By.ID, 'book')
book.click()

def calc(x):
	return str(math.log(abs(12*math.sin(int(x)))))

x_element = browser.find_element(By.ID, 'input_value')
x = x_element.text
y = calc(x)


input1 = browser.find_element(By.ID, 'answer')
input1.send_keys(y)

button = browser.find_element(By.ID, 'solve')
button.click()

# успеваем скопировать код за 30 секунд
time.sleep(10)
	# закрываем браузер после всех манипуляций
browser.quit()

# не забываем оставить пустую строку в конце файла
