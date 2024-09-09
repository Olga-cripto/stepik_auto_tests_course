from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import time
import math
def calc(x):
  return str(math.log(abs(12*math.sin(int(x)))))

try:
    link = 'http://suninjuly.github.io/explicit_wait2.html'
    browser = webdriver.Chrome()
    browser.get(link)
    price = WebDriverWait(browser, 12).until(
        EC.text_to_be_present_in_element((By.ID, "price"),'100')
    )

    btn_book=browser.find_element(By.CSS_SELECTOR, '#book')
    btn_book.click()

    x=browser.find_element(By.CSS_SELECTOR, '#input_value')
    x_text=x.text
    y=calc(x_text)

    input=browser.find_element(By.CSS_SELECTOR, '#answer')
    input.send_keys(y)
    btn_solve=browser.find_element(By.CSS_SELECTOR, '#solve')
    btn_solve.click()


finally:
    # успеваем скопировать код за 30 секунд
    time.sleep(30)
    # закрываем браузер после всех манипуляций
    browser.quit()