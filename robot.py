import time
import math
from selenium import webdriver
from selenium.webdriver.common.by import By

try:
	browser = webdriver.Chrome()
	browser.get("https://suninjuly.github.io/math.html")

	def calc(x):
		return str(math.log(abs(12*math.sin(int(x)))))

	x_element = browser.find_element(By.ID, 'input_value')
	x = x_element.text
	y = calc(x)


	input1 = browser.find_element(By.ID, 'answer')
	input1.send_keys(y)

	option1 = browser.find_element(By.CSS_SELECTOR, "[id='robotCheckbox']")
	option1.click()

	option2 = browser.find_element(By.CSS_SELECTOR, "[id='robotsRule']")
	option2.click()

	button = browser.find_element(By.CSS_SELECTOR, "button.btn")
	button.click()

finally:
	# успеваем скопировать код за 30 секунд
	time.sleep(10)
	# закрываем браузер после всех манипуляций
	browser.quit()

# не забываем оставить пустую строку в конце файла