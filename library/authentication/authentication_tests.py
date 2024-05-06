import time

from selenium import webdriver
from selenium.webdriver.common.by import By


def click_element(browser, locator):
    element = browser.find_element(*locator)
    element.click()


def send_keys_to_element(browser, locator, text):
    element = browser.find_element(*locator)
    element.clear()
    element.send_keys(text)


link = "http://127.0.0.1:8000/"
browser = webdriver.Chrome()
browser.get(link)

login_button_locator = (By.XPATH, '//*[@id="bs-example-navbar-collapse-1"]/ul/li[7]/a')
email_input_locator = (By.XPATH, '//*[@id="id_email"]')
password_input_locator = (By.XPATH, '//*[@id="id_password"]')
submit_button_locator = (By.XPATH, '/html/body/section/div/div/div/div/div/form/div[3]/button')
logout_button_locator = (By.XPATH, '//*[@id="bs-example-navbar-collapse-1"]/ul/li[8]/a')

time.sleep(5)
click_element(browser, login_button_locator)
time.sleep(2)
send_keys_to_element(browser, email_input_locator, 'cooper@gmail.com')
time.sleep(2)
send_keys_to_element(browser, password_input_locator, '1234qwer')
time.sleep(2)
click_element(browser, submit_button_locator)
time.sleep(5)

click_element(browser, logout_button_locator)
time.sleep(5)

click_element(browser, login_button_locator)
time.sleep(2)
send_keys_to_element(browser, email_input_locator, 'cooper5@gmail.com')
time.sleep(2)
send_keys_to_element(browser, password_input_locator, '12345')
time.sleep(2)
click_element(browser, submit_button_locator)
time.sleep(5)

browser.quit()
