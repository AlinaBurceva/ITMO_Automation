from selenium import webdriver
from selenium.webdriver.common.by import By

def test_demoqa():
    driver = webdriver.Chrome()
    driver.get("http://demoqa.com/")

    icon = driver.find_element(By.CSS_SELECTOR, 'header > a > img')

    if icon is None:
        print('Элемент не найден')
    else:
        print('Элемент найден')

    driver.quit()
