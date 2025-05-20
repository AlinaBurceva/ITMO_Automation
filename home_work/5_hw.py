from selenium import webdriver
from selenium.webdriver.common.by import By

def test_saucedemo():
    driver = webdriver.Chrome()
    driver.get("https://www.saucedemo.com/")

    icon = driver.find_element(By.CSS_SELECTOR, '#user-name') \
           and driver.find_element(By.CSS_SELECTOR, '#password') \
           and driver.find_element(By.CSS_SELECTOR, '#login-button')

    if icon is None:
        print('Элементы не найден')
    else:
        print('Элементы найдены')

    driver.quit()